import yfinance as yf
import pandas as pd

# Descargar datos históricos de GameStop
gme_data = yf.download("GME")

# Restablecer el índice para que la columna 'Date' sea una columna normal
gme_data.reset_index(inplace=True)

# Guardar el DataFrame como archivo CSV (opcional)
gme_data.to_csv("gme_data.csv", index=False)

# Mostrar las primeras 5 filas
print(gme_data.head())
