# 🧠 Segmentación de Clientes con FastAPI y Streamlit

Este proyecto permite predecir el segmento de un cliente con base en su ingreso anual y puntaje de gasto, usando un modelo de machine learning previamente entrenado.

Incluye:
- Una **API REST** con FastAPI
- Una **interfaz gráfica** con Streamlit

---

## 🚀 Requisitos

- Python 3.8 o superior (recomendado 3.10+)
- pip
- Git Bash, PowerShell o terminal Bash

---

## 🔧 Instrucciones de Ejecución

### 1. Clona o descarga el proyecto
Ubícate en la carpeta donde estará el proyecto y ejecuta:
```bash
git clone <URL_DEL_REPOSITORIO>
cd nombre-del-proyecto
```

> O simplemente descarga el ZIP y extrae los archivos.

---

### 2. Crea y activa el entorno virtual

#### En PowerShell:
```powershell
python -m venv venv
.env\Scriptsctivate
```

#### En Bash (Git Bash, WSL, etc.):
```bash
python -m venv venv
source venv/Scripts/activate
```

---

### 3. Instala las dependencias
```bash
pip install -r requirements.txt
```

---

### 4. Ejecuta la API
Con el entorno activado, ejecuta:
```bash
python api.py
```

Esto levantará el servidor en:
```
http://localhost:8502
```

Puedes verificar que esté activo ingresando a:
```
http://localhost:8502/docs
```

---

### 5. Ejecuta la app Streamlit (cliente)
En otra terminal (también con el entorno virtual activado):
```bash
streamlit run cliente.py
```

Esto abrirá la app en:
```
http://localhost:8501
```

---

## 🧪 Uso

1. Ingresa el ingreso anual y puntaje de gasto del cliente.
2. Haz clic en “Obtener Segmento”.
3. Verás en pantalla el segmento asignado por el modelo.

---

## 📌 Notas

- Asegúrate de que la API (`api.py`) esté corriendo **antes** de iniciar `cliente.py`.
- Ambos servicios (API y cliente) deben estar activos al mismo tiempo para que funcionen correctamente.
