#Archivo pipeline
# -*- coding: utf-8 -*-
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import sys
import os

#Agrego la carpeta raíz al path de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.transformers import numeroAString, AtributosTemporales, EliminarColumnas, mapeoABarrios

def build_full_pipeline(cat_cols, num_cols, num_a_quitar, df_zonas):
    
    #Pipeline para las numéricas
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('std_scaler', StandardScaler())
    ])
    
    #Pipeline para las categóricas
    cat_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="most_frequent")),
        ('one_hot', OneHotEncoder(handle_unknown='ignore'))
    ])

    #Transformador principal
    full_transformer = ColumnTransformer([
        ('num_tr', num_pipeline, num_cols),
        ('cat_tr', cat_pipeline, cat_cols),
    ], remainder='drop')

    #Retorno el pipeline completo
    return Pipeline([
        ('mapeo', mapeoABarrios(df_zonas)), # <--- Ahora podés usar df_zonas aquí
        ('eliminador', EliminarColumnas(columnas_a_eliminar=num_a_quitar)),
        ('atributos_tiempo', AtributosTemporales(columna_fecha='tpep_pickup_datetime')),
        ('convertidor_str', numeroAString()),
        ('transformation', full_transformer),
    ])