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

## Instalar UV

UV es un gestor de paquetes de Python rápido y moderno. Si no lo tienes instalado, puedes instalarlo con:

```bash
# En macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# En Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Con pip (alternativa)
pip install uv
```

Más información: https://github.com/astral-sh/uv

## Extensiones extras:
- Ruff
- Ty
- Darktheme de Devin de Cognition (antes windsurf)

## Instalación con UV

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/johnometalman/johnometalman-fastapi.git
   puedes renombrar la carpeta como desees
   ```

2. **Instalar dependencias con UV**:
   ```bash
   uv sync
   ```

   Esto creará un entorno virtual e instalará todas las dependencias especificadas en `pyproject.toml`.

## Ejecutar el proyecto

El path del proyecto esta en la carpeta app, por eso app.main

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

## Testing

Ejecutar todos los tests:
```bash
uv run pytest
```

Ejecutar tests con la ruta detallada y con el flag "-v" ejemplo:
```bash
uv run pytest app/tests/test_customers.py -v
```

## Licencia

Este proyecto es solo para fines educativos.
