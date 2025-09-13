import psycopg2
from datetime import datetime
from variables import DB_CONFIG

def inicializar_db():
    """
    Se conecta a la base de datos usando DB_CONFIG y crea la tabla
    'preguntas_respuestas' si esta no existe.
    """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS preguntas_respuestas (
        id SERIAL PRIMARY KEY,
        pregunta TEXT NOT NULL,
        respuesta TEXT NOT NULL,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                cursor.execute(create_table_query)
        print("Conexión exitosa. Tabla 'preguntas_respuestas' lista.")
    except psycopg2.OperationalError as e:
        print(f"Error de conexión: No se pudo conectar a la base de datos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def guardar_conversacion(pregunta, respuesta):
    """
    Guarda una nueva pregunta y respuesta en la base de datos usando DB_CONFIG.
    """
    insert_query = "INSERT INTO preguntas_respuestas (pregunta, respuesta, fecha) VALUES (%s, %s, %s);"
    
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                cursor.execute(insert_query, (pregunta, respuesta, datetime.now()))
        return "ok"
    except Exception as e:
        print(f"Error al guardar en la base de datos: {e}")
        return "error"