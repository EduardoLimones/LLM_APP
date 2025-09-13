import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_endpoint_recomendacion_success():
    """
    Prueba que el endpoint /recomendacion funciona correctamente
    cuando se le envía una pregunta válida.
    """
    url = f"{BASE_URL}/recomendacion"
    payload = {"pregunta": "Recomiéndame un buen juego de estrategia"}

    # Enviamos la petición POST a nuestra API
    response = requests.post(url, json=payload)

    # Verificamos que la respuesta es la esperada
    
    assert response.status_code == 200

    # La respuesta debe ser un JSON que contiene la clave "respuesta"
    response_data = response.json()
    assert "respuesta" in response_data

    # El valor de "respuesta" debe ser un string y no estar vacío
    assert isinstance(response_data["respuesta"], str)
    assert len(response_data["respuesta"]) > 0

def test_endpoint_guia_bad_request():
    """
    Prueba que un endpoint (ej: /guia) devuelve un error 400
    si no se le envía una pregunta en el cuerpo de la petición.
    """
    url = f"{BASE_URL}/guia"
    payload = {}  # Enviamos un cuerpo vacío a propósito

    response = requests.post(url, json=payload)

    # Verificamos que la respuesta es un error de cliente (400 Bad Request)
    assert response.status_code == 400

    # Verificamos que el JSON de error contiene la clave "error"
    response_data = response.json()
    assert "error" in response_data