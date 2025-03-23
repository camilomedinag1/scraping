import yfinance as yf
import pandas as pd

# Descargar los datos históricos de Tesla
tesla_data = yf.download('TSLA')

# Restablecer el índice para convertir la columna de fecha en una columna normal
tesla_data.reset_index(inplace=True)

# Guardar los datos en un archivo CSV (opcional)
tesla_data.to_csv('tesla_data.csv', index=False)

# Mostrar las 5 primeras filas del DataFrame
print(tesla_data.head())
