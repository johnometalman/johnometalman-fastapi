"""
ARCHIVO: conftest.py
PROPÓSITO: Configuración global para todos los tests de pytest.
           pytest busca automáticamente este archivo en el directorio actual y padres.
           Los fixtures definidos aquí están disponibles para TODOS los archivos test_*.py
"""

import pytest
from fastapi.testclient import TestClient 
from sqlmodel import create_engine, SQLModel, Session
from sqlalchemy.pool import StaticPool
from app.main import app
from db import get_session

# ============================================================================
# CONFIGURACIÓN DE BASE DE DATOS PARA TESTS
# ============================================================================

# Nombre del archivo SQLite para pruebas (puede ser diferente al de producción)
sqlite_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_name}"

# Creamos un motor de base de datos ESPECÍFICO para pruebas
# - check_same_thread=False: Permite usar SQLite con múltiples hilos (necesario para FastAPI)
# - StaticPool: Mantiene una sola conexión, no crea nuevas para cada test
engine_test = create_engine(
    sqlite_url, 
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)
    

# ============================================================================
# FIXTURE: session_test
# ============================================================================

@pytest.fixture(name="session_test")
def session_fixture():
    """
    Fixture que proporciona una sesión de base de datos para los tests.
    
    FLUJO:
    1. ANTES del test: Crea TODAS las tablas en la BD (vacías)
    2. DURANTE el test: Entrega una sesión para que el test la use
    3. DESPUÉS del test: Borra TODAS las tablas (limpia todo)
    
    EJEMPLO DE USO:
    def test_create_customer(session_test):
        customer = Customer(name="Juan")
        session_test.add(customer)
        session_test.commit()
        assert customer.id is not None
    """
    # Setup: Crear tablas antes del test
    SQLModel.metadata.create_all(engine_test)
    
    # Crear sesión y entregarla al test
    with Session(engine_test) as session:
        yield session  # El test usa esta sesión
    
    # Teardown: Borrar tablas después del test
    SQLModel.metadata.drop_all(engine_test)


# ============================================================================
# FIXTURE: client_test
# ============================================================================

@pytest.fixture(name="client_test")
def client_fixture(session_test: Session):
    """
    Fixture que proporciona un cliente HTTP de prueba para simular peticiones a la API.
    
    ¿QUÉ HACE?
    1. SOBRESCRIBE la dependencia get_session() para que use la sesión de prueba
    2. Crea un TestClient que simula peticiones HTTP sin necesidad de ejecutar uvicorn
    3. Limpia las dependencias sobrescritas después del test
    
    ¿POR QUÉ ES IMPORTANTE?
    - Los tests usan una BD de prueba (no tocan la BD real)
    - No necesitas ejecutar el servidor para probar los endpoints
    
    EJEMPLO DE USO:
    def test_create_customer(client_test):
        response = client_test.post("/customers/", json={...})
        assert response.status_code == 201
    """
    
    # ========================================================================
    # SOBRESCRITURA DE DEPENDENCIAS (CRUCIAL PARA LOS TESTS)
    # ========================================================================
    
    # Normalmente, FastAPI llama a get_session() para obtener la conexión a DB
    # En los tests, REEMPLAZAMOS get_session() por get_session_overwrite()
    # get_session_overwrite() devuelve la sesión de prueba, no la real
    def get_session_overwrite():
        """Versión de prueba de get_session() que usa la sesión de prueba"""
        return session_test
    
    # Sobrescribimos la dependencia original por la versión de prueba
    app.dependency_overrides[get_session] = get_session_overwrite
    
    # ========================================================================
    # CREACIÓN DEL CLIENTE DE PRUEBA
    # ========================================================================
    
    # TestClient simula un navegador/cliente HTTP
    # - Hace peticiones a tu app "en memoria" (sin necesidad de servidor)
    # - Todas las peticiones usan la sesión de prueba (gracias al override)
    client = TestClient(app)
    
    # Entregar el cliente al test
    yield client
    
    # ========================================================================
    # LIMPIEZA DESPUÉS DEL TEST
    # ========================================================================
    
    # Restaurar las dependencias originales para no afectar otros tests
    app.dependency_overrides.clear()