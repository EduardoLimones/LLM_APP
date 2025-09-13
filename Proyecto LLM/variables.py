import os
from dotenv import load_dotenv

load_dotenv()

# 1. Leemos la API_KEY directamente
API_KEY = os.getenv('API_KEY')

# 2. Leemos las variables de la BBDD y las montamos en el diccionario que nuestros otros scripts esperan.
DB_CONFIG = {
    "host": os.getenv('DB_HOST'),
    "user": os.getenv('DB_USER'),
    "password": os.getenv('DB_PASSWORD'),
    "port": os.getenv('DB_PORT'),
    "dbname": os.getenv('DB_NAME')
}