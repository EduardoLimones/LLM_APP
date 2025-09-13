from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Importamos las funciones especializadas de nuestros otros scripts
from logica_llm import obtener_recomendacion, obtener_nota_y_resena, obtener_guia_y_truco
from gestion_bbdd import guardar_conversacion, inicializar_db

# --- Configuración de la Aplicación ---
app = Flask(__name__)
CORS(app)

# --- Rutas de la API ---

@app.route('/')
def index():
    """
    Ruta principal que en el futuro servirá nuestro archivo index.html.
    """
    # Flask buscará 'index.html' en una carpeta llamada 'templates'
    return render_template('index.html')


@app.route('/recomendacion', methods=['POST'])
def pedir_recomendacion():
    """
    Endpoint para la sección de recomendaciones.
    """
    datos = request.json
    if not datos or 'pregunta' not in datos:
        return jsonify({"error": "No se proporcionó una pregunta."}), 400

    pregunta = datos['pregunta']
    
    # 1. Llamamos a la función del LLM para obtener la respuesta
    respuesta = obtener_recomendacion(pregunta)
    
    # 2. Guardamos la conversación en la base de datos
    guardar_conversacion(pregunta, respuesta)
    
    # 3. Devolvemos la respuesta al front-end
    return jsonify({"respuesta": respuesta})


@app.route('/resena', methods=['POST'])
def pedir_resena():
    """
    Endpoint para la sección de notas y reseñas.
    """
    datos = request.json
    if not datos or 'pregunta' not in datos:
        return jsonify({"error": "No se proporcionó una pregunta."}), 400

    pregunta = datos['pregunta']
    
    # 1. Llamamos a la función del LLM
    respuesta = obtener_nota_y_resena(pregunta)
    
    # 2. Guardamos en la BBDD
    guardar_conversacion(pregunta, respuesta)
    
    # 3. Devolvemos al front-end
    return jsonify({"respuesta": respuesta})


@app.route('/guia', methods=['POST'])
def pedir_guia():
    """
    Endpoint para la sección de guías y trucos.
    """
    datos = request.json
    if not datos or 'pregunta' not in datos:
        return jsonify({"error": "No se proporcionó una pregunta."}), 400

    pregunta = datos['pregunta']
    
    # 1. Llamamos a la función del LLM
    respuesta = obtener_guia_y_truco(pregunta)
    
    # 2. Guardamos en la BBDD
    guardar_conversacion(pregunta, respuesta)
    
    # 3. Devolvemos al front-end
    return jsonify({"respuesta": respuesta})

# --- Ejecución de la Aplicación ---
if __name__ == '__main__':
    # Antes de iniciar la aplicación, nos aseguramos de que la tabla en la BBDD existe.
    inicializar_db()
    # Ejecutamos el servidor de desarrollo de Flask.
    app.run(host='0.0.0.0', port=5000, debug=True)