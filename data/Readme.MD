# 🚖 Información del Dataset: NYC Taxi Trip Duration

Para realizar los retos de este módulo, utilizaremos datos reales de movilidad urbana. Debido al volumen de la información (Big Data), el archivo **no está incluido en este repositorio**.

## 📥 Fuente Oficial
Los datos provienen de la competencia oficial de Kaggle: **NYC Taxi Trip Duration**.

👉 **[Descargar Dataset Aquí](https://www.kaggle.com/competitions/nyc-taxi-trip-duration/data)**

## ⚙️ Instrucciones de Configuración

1.  **Registro:** Debes tener una cuenta en Kaggle (es gratuito).
2.  **Descarga:** Ve a la pestaña "Data" y descarga el archivo `train.zip`.
3.  **Descompresión:** Extrae el archivo en la carpeta `data/` o en la misma raíz donde guardarás tu Jupyter Notebook.
4.  **Archivo Objetivo:** El archivo que usaremos para **todos** los retos es:
    * 📄 `train.csv` (Aprox. 1.4 millones de filas).

> **⚠️ Importante:** El objetivo del reto es lidiar con problemas de memoria RAM y optimización. No intentes abrir este archivo en Excel; úsalo directamente desde Pandas.

## dictionary Diccionario de Datos (Resumen)
* `id`: Identificador único del viaje.
* `vendor_id`: Proveedor del servicio (1 o 2).
* `pickup_datetime`: Fecha y hora de inicio.
* `passenger_count`: Número de pasajeros.
* `pickup_longitude` / `pickup_latitude`: Coordenadas de inicio.
* `dropoff_longitude` / `dropoff_latitude`: Coordenadas de fin.
* `store_and_fwd_flag`: Bandera de conexión ('Y'/'N').
* `trip_duration`: Duración del viaje en segundos (Target).