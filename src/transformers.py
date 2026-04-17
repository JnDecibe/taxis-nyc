#Archivo transformers
# -*- coding: utf-8 -*-
from sklearn.base import BaseEstimator, TransformerMixin

class mapeoABarrios(BaseEstimator, TransformerMixin):
    
    def __init__(self, df_zonas):
        self.df_zonas = df_zonas
    
    def fit(self, X, y=None):
        return self
    
    def mapeo(self, X):
        X_copy = X.copy()
        #Mapeo el origen (PULocationID)
        X_copy = X_copy.merge(self.df_zonas, left_on="PULocationID", right_on="LocationID", how="left")
        
        #Renombro las columnas nuevas
        X_copy.rename(columns={"Borough": "PU_Borough", "Zone": "PU_Zone"}, inplace=True)
        X_copy.drop('LocationID', axis=1, inplace=True) #Borro el ID repetido
        
        #Mapeo el destino (DOLocationID)
        X_copy = X_copy.merge(self.df_zonas, left_on="DOLocationID", right_on="LocationID", how="left")
        X_copy.rename(columns={"Borough": "DO_Borough", "Zone": "DO_Zone"}, inplace=True)
        X_copy.drop("LocationID", axis=1, inplace=True) #Nuevamente, borro el ID repetido.
        
        X_copy.rename(columns={
            "service_zone_x": "PU_service_zone",
            "service_zone_y": "DO_service_zone"
        }, inplace=True)
        
        return X_copy
        
class numeroAString(BaseEstimator, TransformerMixin):
    """
        Extrae strings de números: 
            VendorID, passenger_count, 
            RatecodeID, improvement_surcharge, airport_fee
    """
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X_copy = X.copy()
        #X es un DataFrame acá porque será el primer paso del pipeline
        
        cols_to_str = ["VendorID", "passenger_count", "RatecodeID", "improvement_surcharge", "airport_fee"]
        
        #Solo transformo si la columna existe en el DataFrame actual
        for col in cols_to_str:
            if col in X_copy.columns:
                X_copy[col] = X_copy[col].astype(str)
        return X_copy