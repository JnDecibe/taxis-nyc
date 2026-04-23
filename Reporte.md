# Reporte de Entrenamiento y Evolución del Modelo

Este documento detalla el proceso iterativo para la predicción de propinas en el dataset de NYC Taxi, documentando las mejoras desde la línea base hasta el modelo final.

## Resumen de Progreso
| Iteración | Estrategia | RMSE | Estado |
| :--- | :--- | :--- | :--- |
| **V1** | Variables base + Sin limpieza | $2.29 | Obsoleto |
| **V2** | + Atributos temporales | $2.26 | Obsoleto |
| **V3 (Actual)** | **+ Sanitización + Mapeo + Random Forest** | **$0.78** | **Mejor Modelo** |

---

## Historial de Experimentos

### 1. Primera y Segunda Combinación (Línea Base)
**Variables:** `tolls_amount`, `fare_amount`, `trip_distance`, `PU_Borough`, `DO_Borough`, `RatecodeID`, `hora`, `dia_semana`.

* **Resultados:**
    * Regresión Lineal: $2.28
    * Decision Tree (CV Mean): $2.26
* **Conclusión inicial:** El modelo presentaba un error elevado. Se identificó que el ruido aleatorio y la falta de limpieza de datos atípicos impedían que el modelo capturara patrones reales.

---

## Iteración Actual: Optimización de Ingeniería de Datos

En esta etapa se implementó un cambio de arquitectura en el procesamiento de datos, logrando una reducción del error del **65% respecto a la V2**.

### Cambios Clave:
1.  **Sanitización Automática (`DataSanitizer`):** Se filtraron viajes inconsistentes (tarifas $0, distancias negativas o barrios desconocidos).
2.  **Pipeline de Inferencia:** Se integró el mapeo de zonas y la transformación de variables en un único objeto de Scikit-Learn para evitar el *Data Leakage*.
3.  **Filtrado de Cardinalidad:** Se priorizaron categorías con menos de 10 niveles (Boroughs vs Zones) para mejorar la eficiencia del modelo.

### Resultados Finales:

| Modelo | RMSE Medio | Desviación Estándar |
| :--- | :--- | :--- |
| **Linear Regression** | $1.16 | $0.01 |
| **Decision Tree** | $1.12 | $0.01 |
| **Random Forest** | **$0.78** | **$0.01** |

> **Nota Técnica:** El salto en el desempeño del Random Forest se debe a su capacidad para manejar relaciones no lineales entre la tarifa y la ubicación geográfica, una vez que el ruido de los datos fue eliminado por el Sanitizer.

---

## Conclusiones Finales
* **La limpieza superó a la cantidad:** Eliminar datos basura fue más efectivo que agregar docenas de variables nuevas.
* **Estabilidad:** La baja desviación estándar ($0.01) confirma que el modelo generaliza bien en diferentes particiones del dataset de Nueva York.