import os
from fastapi import FastAPI
import joblib
import pandas as pd

#****************Para la conexión con el Frontend.*******************
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Taxi Trip Tip Predictor")

# Configuración de CORS para que el HTML pueda hablar con la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En producción se pone la URL real, para desarrollo "*" está bien
    allow_methods=["*"],
    allow_headers=["*"],
)
#*********************************************************************

#Importo los transformadores para que el Pipeline sepa qué hacer
from src.transformers import AtributosTemporales, numeroAString 

app = FastAPI(title="Taxi Trip Tip Predictor")

#Cargo el modelo con ruta absoluta para evitar fallos de CWD
ruta_absoluta = os.path.join(os.path.dirname(__file__), 'models', 'modelo_taxis_v1.pkl')

try:
    modelo = joblib.load(ruta_absoluta)
    # Verificación de integridad del objeto
    if not hasattr(modelo, 'predict'):
        print("ERROR: El archivo .pkl se cargó pero no es un Pipeline completo.")
        modelo = None # Evita que la API intente usar un objeto roto
except Exception as e:
    print(f"ERROR AL CARGAR EL MODELO: {e}")
    modelo = None

@app.get("/")
def home():
    return {"mensaje": "API de Predicción de Propinas de NYC activa"}

@app.post("/predict")
def predict(datos: dict):
    if modelo is None:
        return {"error": "El modelo no está cargado en el servidor."}
    
    try:
        # Convertimos el diccionario recibido en un DataFrame
        df_input = pd.DataFrame([datos])
        
        # DEBUG para ver qué llega desde el Swagger
        print(f"DEBUG - Columnas recibidas: {df_input.columns.tolist()}")
        
        # Realizo la predicción
        prediccion = modelo.predict(df_input)
        
        return {
            "prediccion_propina": float(prediccion[0]),
            "unidad": "USD"
        }
    
    except Exception as e:
        # Esto te dirá exactamente qué columna falta o qué falló
        return {"error": str(e), "tipo": str(type(e))}