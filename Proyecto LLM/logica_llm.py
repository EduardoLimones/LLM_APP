import requests
import json
from variables import API_KEY 

# La URL base de la API de Gemini
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"

def _llamar_a_gemini(prompt_completo):
    """
    Función interna y reutilizable para hacer la llamada a la API de Gemini.
    """
    headers = {'Content-Type': 'application/json'}
    body = {"contents": [{"parts": [{"text": prompt_completo}]}]}
    
    try:
        response = requests.post(GEMINI_API_URL, headers=headers, data=json.dumps(body), timeout=45)
        response.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        response_json = response.json()
        
        # Manejo de casos donde la respuesta puede estar vacía o bloqueada
        if 'candidates' not in response_json or not response_json['candidates']:
            return "El modelo no pudo generar una respuesta. Inténtalo de nuevo."
            
        return response_json['candidates'][0]['content']['parts'][0]['text'].strip()

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión al llamar a la API de Gemini: {e}")
        return "Error: No se pudo conectar con el servicio de IA."
    except (KeyError, IndexError):
        return "Error al procesar la respuesta del modelo de IA."

# --- Función 1: Recomendaciones ---
def obtener_recomendacion(pregunta_usuario):
    instruccion_sistema = """
    Eres un asistente experto únicamente en recomendar videojuegos.
    Tu única función es sugerir juegos basados en los gustos del usuario.
    - Si el usuario te pide una guía, truco, nota o reseña, amablemente dile: "Para eso, te recomiendo usar la sección de 'Guías y Trucos' o 'Notas y Reseñas'."
    - Si el usuario pregunta por algo que no sea de videojuegos, responde únicamente: "Lo siento, solo puedo ayudarte con temas de videojuegos."
    """
    prompt = f"{instruccion_sistema}\n\nPREGUNTA DEL USUARIO:\n'{pregunta_usuario}'"
    return _llamar_a_gemini(prompt)

# --- Función 2: Notas y Reseñas ---
def obtener_nota_y_resena(pregunta_usuario):
    instruccion_sistema = """
    Eres un asistente experto únicamente en proporcionar notas, puntuaciones y reseñas de videojuegos.
    Tu única función es dar datos objetivos sobre juegos que el usuario te pida.
    - Si el usuario te pide una recomendación, una guía o un truco, amablemente dile: "Para eso, te recomiendo usar la sección de 'Recomendaciones' o 'Guías y Trucos'."
    - Si el usuario pregunta por algo que no sea de videojuegos, responde únicamente: "Lo siento, solo puedo ayudarte con temas de videojuegos."
    """
    prompt = f"{instruccion_sistema}\n\nPREGUNTA DEL USUARIO:\n'{pregunta_usuario}'"
    return _llamar_a_gemini(prompt)

# --- Función 3: Guías y Trucos ---
def obtener_guia_y_truco(pregunta_usuario):
    instruccion_sistema = """
    Eres un asistente experto únicamente en proporcionar guías, trucos y soluciones para videojuegos.
    Tu única función es ayudar a los jugadores que están atascados o quieren optimizar su partida.
    - Si el usuario te pide una recomendación, una nota o una reseña, amablemente dile: "Para eso, te recomiendo usar la sección de 'Recomendaciones' o 'Notas y Reseñas'."
    - Si el usuario pregunta por algo que no sea de videojuegos, responde únicamente: "Lo siento, solo puedo ayudarte con temas de videojuegos."
    """
    prompt = f"{instruccion_sistema}\n\nPREGUNTA DEL USUARIO:\n'{pregunta_usuario}'"
    return _llamar_a_gemini(prompt)