# Proyecto de Segmentación de Clientes

Este proyecto utiliza un modelo de machine learning para clasificar clientes en diferentes segmentos a partir de su ingreso anual y puntaje de gasto. La aplicación está compuesta por una API construida con **FastAPI**, una interfaz de usuario con **Streamlit** y un backend de entrenamiento distribuido usando **Ray**.

---

## 📦 Requisitos previos

- Python 3.10+
- Docker y Docker Compose
- Cuenta en AWS (EC2)
- Git

---

## 🔧 Instalación local

1. **Clona el repositorio**:

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

2. **Crea y activa un entorno virtual**:

```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Bash/Mac:
source venv/bin/activate
```

3. **Instala las dependencias**:

```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución local

### 1. Iniciar la API con FastAPI:

```bash
cd api
python api.py
```

La API estará disponible en: [http://localhost:8502](http://localhost:8502)

---

### 2. Ejecutar la interfaz con Streamlit:

En una nueva terminal (con el entorno virtual activado):

```bash
cd cliente
streamlit run cliente.py
```

---

## 🐳 Despliegue con Docker y AWS EC2

### 1. Instalar Docker en tu máquina o instancia EC2

Para instalar Docker en Ubuntu:

```bash
sudo apt update
sudo apt install docker.io docker-compose -y
sudo systemctl start docker
sudo systemctl enable docker
```

### 2. Clonar el repositorio en tu EC2:

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

### 3. Construir e iniciar los servicios con Docker Compose:

```bash
sudo docker-compose up --build -d
```

Esto levantará la API y la interfaz de Streamlit. Asegúrate de abrir los puertos necesarios en tu instancia EC2 (por ejemplo, 8501 y 8502).

---

## 📁 Estructura del Proyecto

```
├── api/
│   ├── api.py
│   ├── Dockerfile
├── cliente/
│   ├── cliente.py
│   ├── Dockerfile
├── ray/
│   ├── entrenar_con_ray.py
│   ├── entrenar_modelo.py
├── modelo_segmentacion.joblib
├── docker-compose.yml
├── requirements.txt
├── README.md
```

---

## 🧪 Tecnologías utilizadas

- Python
- FastAPI
- Streamlit
- Ray
- Docker
- Docker Compose
- AWS EC2

---

## ✍️ Autores

- Integrante 1 – API y modelo
- Integrante 2 – Interfaz y cliente
- Integrante 3 – Docker y despliegue
- Integrante 4 – Benchmarking y paralelización

---

## 📜 Licencia

MIT