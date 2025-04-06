
# 🏦 Predicción de Quiebra de Empresas con Azure Machine Learning

Este repositorio contiene un flujo completo de Machine Learning para predecir la quiebra de empresas, desde el entrenamiento del modelo hasta su despliegue como API en Azure y su consumo con datos reales.


## Integrantes

* Jose Abraham Martinez Licona

* Sabrina Carselle Aldaco 

* Andres Morones Navarro 

* Fernanda Alanis Motfort 

* Juan Pablo Sada San Jose 

* Juan Pablo Ramírez Sobrepera

---

## ⚙️ Requisitos

### 🐍 Python
- Versión: Python 3.8 o superior

### 📦 Instalación de dependencias

Instala las librerías necesarias ejecutando:

```bash
pip install -r requirements.txt
```

Contenido del archivo `requirements.txt`:

```
# Core dependencies
pandas
scikit-learn
kagglehub
pickle-mixin

# Azure ML SDK core
azureml-core

# Optional: useful for compatibility with some packages
numpy>=1.19,<1.25
cryptography==41.0.3
```

---

## 📁 Archivos necesarios

Asegúrate de tener en la raíz del proyecto:

- `id.json` → con tu Azure Subscription ID:
```json
{
  "azure_id": "AQUI_TU_ID_DE_SUSCRIPCION"
}
```

- `prueba.csv` → datos reales para hacer predicción.
- `model.pkl` → archivo generado tras entrenar el modelo.
- `uri.json` → archivo generado al desplegar el modelo (contiene la URL del endpoint).
- `requirements.txt` → lista de dependencias.

---

## 🚀 PASOS PARA EJECUTAR EL PROYECTO

---

### 1️⃣ Entrenar el modelo (`TrainModel.ipynb`)

Este notebook realiza:

1. Descarga el dataset desde Kaggle con `kagglehub`.
2. Elimina variables constantes con `VarianceThreshold`.
3. Selecciona las mejores columnas usando `SelectKBest` y F-score.
4. Entrena un modelo SVM (`SVC`) con kernel RBF.
5. Evalúa el modelo con `classification_report`.
6. Guarda el modelo entrenado como `model.pkl`.

> ✅ Este archivo se necesita para el despliegue en Azure.

---

### 2️⃣ Desplegar el modelo en Azure (`Deployer.ipynb`)

Este notebook:

1. Carga tu ID de suscripción desde `id.json`.
2. Crea un `Workspace` en Azure (si no existe).
3. Registra el modelo entrenado (`model.pkl`) en Azure ML.
4. Genera el archivo `score.py` con la lógica para procesar predicciones.
5. Define el entorno de ejecución (`pandas`, `scikit-learn`, `joblib`, etc.).
6. Despliega el modelo en un contenedor ACI (`Azure Container Instance`).
7. Guarda la URI del endpoint en `uri.json`.

> ⏳ Este paso tarda unos minutos. Al finalizar, tu modelo estará disponible como API REST.

---

### 3️⃣ Consumir la API (`API.ipynb`)

Este notebook:

1. Carga el archivo `prueba.csv` (datos reales).
2. Elimina columnas innecesarias y limpia los nombres.
3. Verifica que todas las columnas requeridas por el modelo estén presentes.
4. Convierte los datos a JSON con el formato que espera Azure.
5. Lee la URI del endpoint desde `uri.json`.
6. Envía los datos al modelo usando `requests`.
7. Recibe las predicciones y las agrega al DataFrame en una nueva columna: `Bankcrupt`.

> 🔁 Puedes ejecutar este paso varias veces con diferentes archivos `prueba.csv`.

---

## 🗂 Estructura del proyecto

```
.
├── TrainModel.ipynb         # Entrenamiento del modelo
├── Deployer.ipynb           # Registro y despliegue en Azure
├── API.ipynb                # Consumo de la API con datos reales
├── score.py                 # Lógica de inferencia usada por Azure
├── model.pkl                # Modelo entrenado (generado en el paso 1)
├── prueba.csv               # Archivo de datos reales para predicción
├── uri.json                 # URI del endpoint generado (se crea en el paso 2)
├── id.json                  # ID de suscripción de Azure
├── requirements.txt         # Dependencias
└── README.md                # Este archivo :)
```

---

## 🧠 Tips útiles

- Si tienes errores de despliegue por **cuotas de CPU**, cambia la región de `"centralindia"` a otra como `"eastus"` o `"westeurope"` en `Deployer.ipynb`.
- El archivo `score.py` debe tener las **mismas columnas y orden** que las usadas en el entrenamiento.
- Puedes personalizar los datos de `prueba.csv` con tus propios ejemplos reales.

---

## 📬 Contacto

Este proyecto fue desarrollado con fines educativos y prácticos.  
Si tienes dudas o sugerencias, ¡no dudes en crear un issue o pull request!
# cloud_computing_semana_2
# cloud_computing
