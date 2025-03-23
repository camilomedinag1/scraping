# Importar librerías necesarias
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Descargar datos históricos de GameStop (GME)
gme_data = yf.download('GME')

# Restablecer el índice para tener 'Date' como columna
gme_data.reset_index(inplace=True)

# Función para graficar los precios de cierre
def make_graph(stock_data, stock, title):
    plt.figure(figsize=(14, 6))
    plt.plot(stock_data['Date'], stock_data['Close'], label=stock, color='purple')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Stock Price (USD)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Llamar a la función para graficar GameStop
make_graph(gme_data, stock='GME', title='GameStop Stock Price Over Time')
