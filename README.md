# 🎮 Asistente IA de Videojuegos 🤖

¡Bienvenido! Este proyecto es una aplicación web full-stack que funciona como un asistente inteligente y especializado en el universo de los videojuegos. Utiliza el poder del modelo de lenguaje grande (LLM) de Google, **Gemini**, para ofrecer respuestas expertas en tres áreas: recomendaciones, análisis de notas/reseñas y guías/trucos.

El proyecto está completamente **dockerizado** para un despliegue fácil y consistente, y se conecta a una base de datos **PostgreSQL** en la nube para registrar el historial de conversaciones.

---
## 🏛️ Arquitectura

La aplicación sigue una arquitectura desacoplada, asegurando que cada componente sea independiente y fácil de mantener.

* **🖥️ Frontend**: Una interfaz de usuario limpia construida con **HTML, CSS y JavaScript**.
* **⚙️ Backend (API)**: Una API RESTful robusta creada con **Flask (Python)** que actúa como el cerebro, orquestando las peticiones del usuario, la lógica de la IA y la persistencia de datos.
* **🧠 Lógica del LLM**: Un módulo especializado en Python que se encarga de construir prompts inteligentes y comunicarse directamente con la **API de Gemini**.
* **💾 Base de Datos**: Un módulo de persistencia que maneja todas las transacciones con una base de datos **PostgreSQL** externa.

---
## ✨ Tecnologías Utilizadas

Una selección de tecnologías modernas para construir una aplicación robusta y escalable.

| Categoría         | Tecnología                                                                                             |
| :---------------- | :----------------------------------------------------------------------------------------------------- |
| **Backend** | 🐍 Python, Flask                                                                                       |
| **Base de Datos** | 🐘 PostgreSQL                                                                                         |
| **IA & LLM** | 🧠 Google Gemini API                                                                                   |
| **Frontend** | 🌐 HTML, CSS, JavaScript (Vanilla)                                                                     |
| **Testing** | ✅ Pytest                                                                                              |
| **Contenerización**| 🐳 Docker                                                                                              |
| **Despliegue** | ☁️ Render / AWS                                                                                        |
| **Librerías Clave**| `psycopg2-binary`, `requests`, `python-dotenv`                                                         |

---
## 🛠️ Configuración del Entorno Local

Sigue estos pasos para poner en marcha el proyecto en tu máquina.

### 1️⃣ Clonar el Repositorio
```bash
git clone https://github.com/EduardoLimones/LLM_APP.git
cd LLM_APP
```

### 2️⃣ Crear y Activar Entorno Virtual
```bash
# Crear el entorno
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en macOS/Linux
source venv/bin/activate
```

### 3️⃣ Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar Variables de Entorno
Crea un archivo llamado `.env` en la raíz del proyecto. Este archivo es secreto y no debe subirse a Git. Copia el siguiente contenido y rellénalo con tus credenciales.

```env
# 🤫 Archivo .env - Variables de Entorno

# === Secretos de la Base de Datos PostgreSQL ===
DB_HOST=TU_HOST_DE_AWS_AQUÍ
DB_USER=TU_USUARIO_DE_LA_BBDD_AQUÍ
DB_PASSWORD=TU_CONTRASEÑA_DE_LA_BBDD_AQUÍ
DB_PORT=5432
DB_NAME=EL_NOMBRE_DE_TU_BBDD_AQUÍ

# === Secreto de la API de Gemini ===
API_KEY=TU_API_KEY_DE_GEMINI_AQUÍ
```

---
## 🚀 Cómo Ejecutar la Aplicación

Una vez configurado el entorno, inicia el servidor de Flask.
```bash
python app.py
```
La aplicación estará disponible en `http://127.0.0.1:5000`.

*Nota: La primera vez que se ejecute, se intentará crear la tabla `preguntas_respuestas` en la base de datos si no existe.*

---
## 🔌 Uso de la API

La API expone tres endpoints principales que aceptan peticiones `POST` con un cuerpo JSON.

* `/recomendacion`
* `/resena`
* `/guia`

#### Ejemplo de Petición con `curl`
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"pregunta": "Recomiéndame un buen RPG para PC"}' \
  [http://127.0.0.1:5000/recomendacion](http://127.0.0.1:5000/recomendacion)
```

---
## ✅ Cómo Ejecutar los Tests

Para verificar que la API funciona correctamente:

1.  En una terminal, asegúrate de que la aplicación principal se está ejecutando: `python app.py`.
2.  En una **segunda terminal**, ejecuta `pytest`:
    ```bash
    pytest
    ```

---
## 🐳 Despliegue con Docker

Este proyecto está preparado para ser desplegado con Docker para una máxima portabilidad.

### 1. Construir la Imagen
```bash
docker build -t eduardolimones/mi-asistente-ia:1.0 .
```

### 2. Ejecutar el Contenedor
Asegúrate de pasar las variables de entorno a través del archivo `.env`.
```bash
docker run -d -p 5000:5000 --env-file ./.env --name mi-contenedor eduardolimones/mi-asistente-ia:1.0
```
La aplicación estará disponible en `http://localhost:5000`.

---
## 👨‍💻 Autor

Desarrollado por **Eduardo José Limones Contreras**.

* **LinkedIn**: [Perfil de LinkedIn](https://www.linkedin.com/in/eduardo-jos%C3%A9-limones-contreras-b1348677/)
* **Correo**: `eduardo.limones.contreras@gmail.com`
