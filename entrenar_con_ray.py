import pandas as pd
from sklearn.cluster import KMeans
import joblib
import time
import ray

# 1. Convertimos la función a una "tarea remota" de Ray
@ray.remote
def entrenar_modelo_remoto():
    print("Iniciando entrenamiento en paralelo con Ray...")
    df = pd.read_csv("datos_clientes.csv")
    kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
    kmeans.fit(df)
    # En lugar de guardar, la función ahora devuelve el modelo
    return kmeans

# --- El flujo principal ---
if __name__ == "__main__":
    # 2. Iniciamos Ray
    ray.init()
    start_time = time.time()

    # 3. Ejecutamos la tarea en paralelo
    #    .remote() no la ejecuta inmediatamente, la pone en la cola de Ray
    modelo_futuro = entrenar_modelo_remoto.remote()

    # 4. Obtenemos el resultado cuando esté listo
    #    ray.get() espera a que la tarea termine
    modelo_final = ray.get(modelo_futuro)

    # Guardamos el modelo que recibimos
    joblib.dump(modelo_final, "modelo_segmentacion.joblib")
    print("¡Modelo entrenado con Ray y guardado!")

    end_time = time.time()
    print(f"Tiempo de ejecución con Ray: {end_time - start_time:.4f} segundos")