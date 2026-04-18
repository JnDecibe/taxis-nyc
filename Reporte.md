# Sobre el Modelo:
Actualmente, el modelo presenta un RMSE de USD 2.29, lo cual representa un error elevado considerando que la propina promedio es de USD 2.96. Esto sugiere que el modelo aún no captura variables clave de comportamiento (como temporalidad o tráfico) y se comporta de forma cercana a un predictor de la media.

## Primera combinación de variables y modelos:

### Variables:
columnas_num = ["tolls_amount", "fare_amount", "extra", "trip_distance"]
columnas_cat = ["PU_Borough", "DO_Borough", "RatecodeID","passenger_count", 
                "improvement_surcharge", "Airport_fee"]

### Modelos y sus resultados:
#### Regresión lineal:
    Error promedio (RMSE): 2.2833519332502306
#### Decision Tree:
    Error promedio (RMSE): 2.2088988766870212
    Cross Validation: 
        Scores: [2.27404822 2.35639212 2.23972665 2.30126327 2.28028229]
        Mean: 2.2903425108093236
        Standard deviation: 0.038498031263027394

## Segunda combinación de variables y modelos:

### Variables:
columnas_num = ["tolls_amount", "fare_amount", "extra", "trip_distance"]
columnas_cat = ["PU_Borough", "DO_Borough", "RatecodeID","passenger_count", 
                "improvement_surcharge", "Airport_fee",

                #Agrego dos más para mejorar la precisión del modelo:
                "hora", "dia_semana"
               ]

### Modelos y sus resultados:
#### Regresión lineal:
    Error promedio (RMSE): 2.282105950083071
#### Decision Tree:
    Error promedio (RMSE): 2.2328968537459537

    Cross Validation: 

        Scores: [2.26006005 2.3342084  2.20749846 2.27554486 2.25322765]
        Mean: 2.2661078841508115
        Standard deviation: 0.040900558261319636

## Algunas conclusiones
Si bien los modelos mejoraron, la mejora fue muy baja. Es posible que haya factores que el modelo aún no ve, como:

- La generosidad (Ruido aleatorio): Dos personas en el mismo viaje, a la misma hora, pueden dar propinas muy distintas.

- Duración del viaje: Un viaje de 2 millas que tarda 10 minutos es distinto a uno que tarda 40 minutos por tráfico. 