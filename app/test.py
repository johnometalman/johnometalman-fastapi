"""
ARCHIVO: test.py
PROPÓSITO: Tests unitarios para verificar el comportamiento de la API.
           pytest ejecuta automáticamente todas las funciones que comienzan con "test_"
"""

from fastapi.testclient import TestClient


# ============================================================================
# TEST BÁSICO: Verificar que el cliente funciona
# ============================================================================

def test_client(client_test):
    """
    Test más simple posible para verificar que el fixture client_test funciona.
    
    ¿QUÉ PRUEBA?
    - Que client_test es un objeto de tipo TestClient
    - Que pytest puede inyectar correctamente el fixture
    
    ¿CÓMO FUNCIONA?
    1. pytest ve el parámetro 'client_test'
    2. Busca un fixture con el nombre 'client_test'
    3. Lo encuentra en conftest.py (definido con @pytest.fixture(name="client_test"))
    4. Inyecta el TestClient en el parámetro
    5. Ejecuta el test
    
    NOTA: El nombre del parámetro DEBE coincidir con el nombre del fixture.
          Si usas "ClientTest" (mayúscula) o "otra_cosa", pytest no lo encuentra.
    """
    
    # Verificar que recibimos un TestClient
    assert type(client_test) is TestClient