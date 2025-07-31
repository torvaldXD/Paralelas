import streamlit as st
import requests
import os

st.title("Verificador de Segmento de Cliente")

# URL de nuestra API - Usar variable de entorno o configurar según el entorno
API_HOST = os.getenv('API_HOST', 'localhost')  # Cambiar a la IP pública de EC2 en producción
API_URL = f"http://{API_HOST}:8502/predecir"

# Crear campos para que el usuario ingrese datos
st.write("Ingrese los datos del cliente para saber a qué segmento pertenece:")
ingreso = st.number_input("Ingreso Anual (en miles)", min_value=10, max_value=200, value=50)
puntaje = st.number_input("Puntaje de Gasto (1-100)", min_value=1, max_value=100, value=50)

# Botón para hacer la predicción
if st.button("Obtener Segmento"):
    # Llamar a la API
    try:
        response = requests.post(API_URL, params={"ingreso_anual": ingreso, "puntaje_gasto": puntaje})
        if response.status_code == 200:
            resultado = response.json()
            segmento = resultado["segmento_cliente"]
            st.success(f"🎉 ¡El cliente pertenece al Segmento {segmento}!")
        else:
            st.error(f"Error en la API: {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("😭 No se pudo conectar a la API. ¿Está el contenedor de Docker corriendo?")