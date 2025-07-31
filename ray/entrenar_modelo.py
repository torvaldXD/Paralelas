import pandas as pd
from sklearn.cluster import KMeans
import joblib
import time

def entrenar_y_guardar_modelo():
    print("Iniciando entrenamiento...")
    # 1. Cargar los datos desde el CSV
    df = pd.read_csv("datos_clientes.csv")

    # 2. Crear y entrenar el modelo K-Means
    # Lo configuramos para encontrar 3 grupos (segmentos) de clientes
    kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
    kmeans.fit(df)

    # 3. Guardar el modelo entrenado en un archivo
    joblib.dump(kmeans, "modelo_segmentacion.joblib")
    print("¡Modelo entrenado y guardado en 'modelo_segmentacion.joblib'!")

if __name__ == "__main__":
    # Medimos el tiempo que tarda
    start_time = time.time()
    entrenar_y_guardar_modelo()
    end_time = time.time()
    print(f"Tiempo de ejecución secuencial: {end_time - start_time:.4f} segundos")