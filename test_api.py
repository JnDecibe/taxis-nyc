# -*- coding: utf-8 -*-
import os
import sys
import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#******** AJUSTE DE RUTAS Y REGISTRO DE CLASES ********
ruta_app = os.path.dirname(os.path.abspath(__file__))
if ruta_app not in sys.path:
    sys.path.append(ruta_app)

try:
    import src.transformers as tf
    sys.modules['src.transformers'] = tf
    from src.transformers import (
        mapeoABarrios, 
        EliminarColumnas, 
        AtributosTemporales, 
        numeroAString
    )
    
    # Registro en __main__ para compatibilidad con el guardado del Notebook
    main_module = sys.modules['__main__']
    main_module.mapeoABarrios = mapeoABarrios
    main_module.EliminarColumnas = EliminarColumnas
    main_module.AtributosTemporales = AtributosTemporales
    main_module.numeroAString = numeroAString
    
    print("Clases y transformadores registrados correctamente.")
except ImportError as e:
    print(f"ERROR CRÍTICO al importar transformadores: {e}")

#******** INICIALIZACIÓN DE LA API ********
app = FastAPI(title="Taxi Trip Tip Predictor")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ******** CARGA DEL MODELO ********
ruta_modelo = os.path.join(ruta_app, 'models', 'modelo_final_v6.pkl')

try:
    if os.path.exists(ruta_modelo):
        tamano_mb = os.path.getsize(ruta_modelo) / (1024 * 1024)
        print(f"Cargando: {ruta_modelo} ({tamano_mb:.2f} MB)")
        with open(ruta_modelo, 'rb') as f:
            modelo = joblib.load(f)
        print("¡LOGRADO! Modelo v6 activo.")
    else:
        print(f"ERROR: No se encontró el archivo v6 en {ruta_modelo}")
        modelo = None
except Exception as e:
    import traceback
    print("FALLÓ LA CARGA DEL MODELO:")
    traceback.print_exc()
    modelo = None

# ******** ENDPOINTS ********
@app.get("/")
def home():
    return {
        "mensaje": "API de Predicción de Propinas de NYC activa",
        "modelo_estado": "Cargado" if modelo else "Error en carga",
        "archivo_usado": "modelo_final_v6.pkl"
    }

@app.post("/predict")
def predict(datos: dict):
    if modelo is None:
        return {"error": "El modelo no está disponible."}
    
    try:
        #1. Convierto entrada a DataFrame
        df_input = pd.DataFrame([datos])
        
        #2. Manejo de columnas faltantes exigidas por el Pipeline
        #El modelo espera estas columnas porque estaban presentes en el entrenamiento
        columnas_exigidas = ['cbd_congestion_fee', 'total_amount']
        for col in columnas_exigidas:
            if col not in df_input.columns:
                df_input[col] = 0.0
        
        #3. Predicción
        #Nota: El Pipeline aplicará internamente tus transformadores de 'src'
        prediccion = modelo.predict(df_input)
        
        return {
            "prediccion_propina": round(float(prediccion[0]), 2),
            "unidad": "USD",
            "status": "success"
        }
    except Exception as e:
        return {
            "error": "Error durante la ejecución del Pipeline",
            "detalle": str(e)
        }