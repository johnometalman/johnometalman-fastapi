# Platzi FastAPI Course

⚠️ **AVISO IMPORTANTE**: Este repositorio es exclusivamente para fines educativos y de aprendizaje del curso de FastAPI de Platzi. **NO debe utilizarse en entornos de producción**.

## Descripción

Aplicación de pruebas desarrollada durante el curso de FastAPI de Platzi. Este proyecto sirve como entorno de aprendizaje para practicar conceptos de FastAPI, incluyendo:

- Routers y modularización
- Middleware para logging
- Autenticación básica (HTTP Basic)
- Base de datos con SQLModel
- Testing con pytest

## Requisitos

- Python >= 3.11
- UV (gestor de paquetes de Python)

## Instalación con UV

1. **Clonar el repositorio**:
   ```bash
   git clone <url-del-repositorio>
   cd platzi-course
   ```

2. **Instalar dependencias con UV**:
   ```bash
   uv sync
   ```

   Esto creará un entorno virtual e instalará todas las dependencias especificadas en `pyproject.toml`.

3. **Activar el entorno virtual** (si no se activa automáticamente):
   ```bash
   source .venv/bin/activate  # En macOS/Linux
   # o
   .venv\Scripts\activate     # En Windows
   ```

## Ejecutar el proyecto

```bash
uv run uvicorn app.main:app --reload
```

La aplicación estará disponible en `http://localhost:8000`

## Estructura del proyecto

```
platzi-course/
├── app/
│   ├── main.py           # Aplicación principal FastAPI
│   ├── routers/          # Módulos de rutas
│   │   ├── customers.py
│   │   ├── transactions.py
│   │   ├── invoices.py
│   │   ├── extras.py
│   │   └── plans.py
│   └── test.py
├── db.py                 # Configuración de base de datos
├── models.py             # Modelos de datos
├── conftest.py           # Configuración de pytest
├── pyproject.toml        # Dependencias del proyecto
└── uv.lock               # Lockfile de UV
```

## Dependencias principales

- **FastAPI**: Framework web moderno y rápido
- **Pydantic**: Validación de datos
- **SQLModel**: ORM para bases de datos
- **Uvicorn**: Servidor ASGI

## Dependencias de desarrollo

- **pytest**: Framework de testing
- **httpx2**: Cliente HTTP para pruebas

## Autenticación

El endpoint root (`/`) requiere autenticación básica HTTP:
- Usuario: `johnometalman`
- Contraseña: `123456test`

## Testing

Ejecutar tests:
```bash
uv run pytest
```

## Licencia

Este proyecto es solo para fines educativos.
