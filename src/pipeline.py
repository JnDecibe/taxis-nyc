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

from src.transformers import numeroAString

def build_full_pipeline(cat_cols, num_cols):
    #No incluyo 'cleaning' acá porque borra filas.
    
    #Pipeline para las numéricas: Imputa con la media y luego Escala
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('std_scaler', StandardScaler())
    ])
    
    #Pipeline para las categóricas: Imputa con la moda y luego OneHot
    cat_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="most_frequent")),
        ('one_hot', OneHotEncoder(handle_unknown='ignore'))
    ])

    #Las columnas deben estar definidas antes de crear el ColumnTransformer.

    full_transformer = ColumnTransformer([
        ('num_tr', num_pipeline, num_cols),
        ('cat_tr', cat_pipeline, cat_cols),
    ])

    return Pipeline([
        ('convertidor_str', numeroAString()),
        ('transformation', full_transformer),
    ])