# Descripción de las columnas
Se usó como fuente el diccionario de la página oficial del gobierno de NYC:

https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf

## Sobre el término Tpep que aparece mucho (Gemini): TpepTaxicab Passenger Enhancement Program.

Nombre del sistema tecnológico instalado en los taxis amarillos. Fue una iniciativa de la ciudad para modernizar los vehículos.

¿Qué hace realmente el sistema TPEP? Representa la integración de tres funciones principales que terminan generando datos:

1. Manejo de Pagos: Es el hardware que permite pagar con tarjeta de crédito (por eso las propinas quedan registradas ahí).

2. Pantalla del Pasajero: La pantalla táctil que ves en el asiento trasero con noticias, mapas y el sistema de pago.

3. Transmisión de Datos (LBS): El GPS que rastrea la ubicación del taxi y envía los registros de cada viaje a la base de datos central de la ciudad.

## Sobre las columnas:

- VendorID: Código de la empresa de taxis.

- tpep_pickup_datetime: Fecha y hora exacta en que subió el pasajero.

- tpep_dropoff_datetime: Fecha y hora en que se desactivó el medidor.

- passenger_count: Número de pasajeros en el vehículo.

- trip_distance: Distancia del viaje en millas.

- RatecodeID: El código de tarifa final vigente al final del viaje.

1 = Tarifa estándar
2 = JFK
3 = Newark
4 = Nassau o Westchester
5 = Tarifa negociada
6 = Viaje en grupo
99 = Nulo/desconocido

- store_and_fwd_flag: Esta bandera indica si el registro del viaje se mantuvo en la memoria del vehículo antes de enviarlo al proveedor (almacenamiento y reenvío), ya que el vehículo no tenía conexión con el servidor.

Y = almacenamiento y reenvío del viaje

N = no es un almacenamiento y reenvío del viaje

- PULocationID: TLC (Taxi and Limousine Commission) Zona en la cual se encontraba activado el taxímetro. PU significa Pick-Up (donde el pasajero subió al taxi).

- DOLocationID: TLC Zona en la cual se encontraba desactivado el taxímetro. DO significa Drop-Off (donde el pasajero bajó).

- payment_type: Cómo pagó.

0 = Viaje con tarifa flexible
1 = Tarjeta de crédito
2 = Efectivo
3 = Sin cargo
4 = Disputa
5 = Desconocido
6 = Viaje anulado

- fare_amount: La tarifa por tiempo y distancia calculada por el taxímetro.

- extra: Extra y recargos varios.

- mta_tax: Impuesto que se activa automáticamente en función de la tasa medida en uso.

- tip_amount: Cantidad de propina: Este campo se completa automáticamente para las propinas con tarjeta de crédito. No incluye las propinas en efectivo.

- tolls_amount: Importe total de todos los peajes pagados en el viaje.

- improvement_surcharge: Recargo por mejora: Se aplica un recargo por mejora a los viajes en la bajada de bandera. El recargo por mejora comenzó a aplicarse en 2015.

- total_amount: El importe total cobrado a los pasajeros. No incluye propinas en efectivo.

- congestion_surcharge: Monto total recaudado en el viaje por el recargo por congestión del estado de Nueva York.

- airport_fee: Solo para recogida en los aeropuertos LaGuardia y John F. Kennedy.

- cbd_congestion_fee: Cargo fijo por viaje aplicado a los vehículos que circulan dentro de la Zona de Alivio de Congestión de la MTA (bajo la calle 60 en Manhattan). Implementado a partir del 5 de enero de 2025.

### Información respecto de la columna service_zone (Aparece al hacer el mapeo)

Esta columna clasifica las zonas de Nueva York según el tipo de servicio de taxi que predomina o las reglas de la ciudad. Los valores que se van a encontrar son:

**Yellow Zone:** Principalmente Manhattan (debajo de la calle 110). Son las zonas donde los taxis amarillos tienen exclusividad para levantar pasajeros en la calle.

**Boro Zone:** Zonas fuera del centro de Manhattan (Brooklyn, Queens, Bronx, Staten Island, y el norte de Manhattan). Acá operan tanto taxis amarillos como verdes.

**Airports:** Zonas especiales para los aeropuertos (JFK y LaGuardia). Tienen reglas de tarifas distintas.

**EWR:** Newark Airport (en New Jersey). Es un caso especial porque está fuera de los 5 distritos de NYC.