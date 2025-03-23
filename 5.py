# Importar librerías necesarias
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Descargar datos históricos de Tesla (TSLA)
tesla_data = yf.download('TSLA')

# Restablecer el índice para tener la columna 'Date'
tesla_data.reset_index(inplace=True)

# Función para graficar
def make_graph(stock_data, stock, title):
    plt.figure(figsize=(14, 6))
    plt.plot(stock_data['Date'], stock_data['Close'], label=stock)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Stock Price (USD)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Llamar a la función para graficar Tesla
make_graph(tesla_data, stock='TSLA', title='Tesla Stock Price Over Time')
