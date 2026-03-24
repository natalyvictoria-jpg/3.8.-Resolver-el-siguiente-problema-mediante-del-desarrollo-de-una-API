# 3.8.-Resolver-el-siguiente-problema-mediante-del-desarrollo-de-una-API

# ✅ API Tareas - ITIC

API REST desarrollada en Python con Flask y PostgreSQL para administrar 
tareas personales con un CRUD completo.

## 📋 Descripción

Este proyecto forma parte de la materia **Aplicaciones Web Orientadas 
a Servicios (ITIC 2025-2026)**. El objetivo es implementar un CRUD 
completo y comprender la estructura básica de un servicio REST conectado 
a una base de datos PostgreSQL.

## 🎯 Propósito

Proporcionar un sistema que permita:
- Crear tareas con título, descripción y estado
- Consultar y filtrar tareas por estado o título
- Actualizar el estado y contenido de una tarea
- Eliminar tareas
- Documentar y probar la API visualmente con Swagger

## 🚀 Endpoints

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/api/tareas` | Obtener todas las tareas |
| GET | `/api/tareas?estado=pendiente` | Filtrar por estado |
| GET | `/api/tareas?titulo=Flask` | Buscar por título |
| GET | `/api/tareas/{id}` | Obtener una tarea por ID |
| POST | `/api/tareas` | Crear una nueva tarea |
| PUT | `/api/tareas/{id}` | Actualizar una tarea |
| DELETE | `/api/tareas/{id}` | Eliminar una tarea |

## 📌 Estados válidos

| Estado | Descripción |
|---|---|
| `pendiente` | Tarea recién creada (default) |
| `en progreso` | Tarea en desarrollo |
| `completada` | Tarea finalizada |

## 🛠 Tecnologías

- Python 3.14
- Flask 3.x
- PostgreSQL
- SQLAlchemy + Flask-SQLAlchemy
- Flasgger (Swagger UI)
- Flask-CORS
- python-dotenv

## ⚙️ Instalación
```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/api_tareas.git
cd api_tareas

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependencias
pip install flask flask-sqlalchemy psycopg2-binary python-dotenv flasgger flask-cors
```

## 🔧 Configuración

Crea un archivo `.env` en la raíz del proyecto:
```
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=clave-secreta-api-tareas
DATABASE_URL=postgresql://usuario:password@localhost:5432/api_tareas_db
```

## ▶️ Ejecutar
```bash
python run.py
```

Abre el navegador en `http://localhost:5000` para ver la documentación 
Swagger y probar todos los endpoints.

## 📁 Estructura

| Archivo | Descripción |
|---|---|
| `app/__init__.py` | Configuración principal de Flask |
| `app/models.py` | Modelo Tarea de base de datos |
| `app/routes.py` | Endpoints CRUD de la API |
| `run.py` | Punto de entrada del servidor |
| `.env` | Variables de entorno |

## 📝 Ejemplo de uso

**Crear una tarea:**
```json
POST /api/tareas
{
  "titulo": "Estudiar Flask",
  "descripcion": "Repasar endpoints REST",
  "estado": "pendiente"
}
```

**Actualizar estado:**
```json
PUT /api/tareas/1
{
  "estado": "completada"
}
```

![pruebas](https://github.com/natalyvictoria-jpg/3.7.-Resolver-problema-mediante-una-API/raw/main/ab.jpeg)
