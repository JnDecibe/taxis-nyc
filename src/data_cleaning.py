# -*- coding: utf-8 -*-
class DataSanitizer:
    def __init__(self, df_zonas, limits=None):
        self.df_zonas = df_zonas
        self.limits = limits or {
            "max_fare": 100,
            "max_passengers": 5,
            "max_distance": 50,
            "payment_type": 1
        }

    def clean(self, df):
        #IMPORTANTE: Reseteo el índice para asegurar alineación perfecta
        #(el merge suele romper la correspondencia de los índices originales)
        df_copy = df.copy().reset_index(drop=True)
        
        #Aplico mapeo temporal
        from src.transformers import mapeoABarrios
        mapper = mapeoABarrios(self.df_zonas)
        df_temp = mapper.mapeo(df_copy)
        
        #Genero la máscara
        #(ahora df_temp y df_copy tienen exactamente el mismo orden e índice)
        mask = (
            (df_temp["payment_type"] == self.limits["payment_type"]) &
            (df_temp["fare_amount"] > 0) &
            (df_temp["passenger_count"] > 0) &
            (df_temp["passenger_count"] < self.limits["max_passengers"]) &
            (df_temp["tip_amount"] >= 0) &
            (df_temp["tip_amount"] < self.limits["max_fare"]) &
            (df_temp["trip_distance"] > 0) &
            (df_temp["trip_distance"] < self.limits["max_distance"]) &
            (df_temp["PU_Borough"] != "Unknown") &
            (df_temp["DO_Borough"] != "Unknown")
        )
        
        #Retorno el original filtrado
        #al usar .values en la máscara, me aseguro de que Pandas 
        #trate a la máscara como un array de booleanos puro, evitando el IndexingError
        return df_copy[mask.values].copy()