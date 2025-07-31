from fastapi import FastAPI
import joblib
import uvicorn

# 1. Iniciar la aplicación FastAPI
app = FastAPI(title="API de Segmentación de Clientes")

# 2. Cargar el modelo al inicio
modelo = joblib.load("modelo_segmentacion.joblib")
print("Modelo cargado exitosamente.")

# 3. Definir el endpoint de la API
@app.post("/predecir")
async def predecir(ingreso_anual: int, puntaje_gasto: int):
    # Hacemos la predicción con los datos que nos llegan
    datos_nuevos = [[ingreso_anual, puntaje_gasto]]
    prediccion = modelo.predict(datos_nuevos)

    # Devolvemos el resultado
    # convertimos el resultado de numpy a int para que no haya problemas
    segmento = int(prediccion[0])
    return {"segmento_cliente": segmento}

if __name__ == "__main__":
    # Iniciar el servidor
    uvicorn.run(app, host="0.0.0.0", port=8502)