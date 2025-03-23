import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL de Macrotrends con los ingresos de Tesla
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

# Simular un navegador con headers para evitar el error 403
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Obtener el HTML de la página
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Buscar todas las tablas en la página
tables = soup.find_all("table")

# Buscar la tabla que contiene 'Tesla Quarterly Revenue'
for table in tables:
    if "Tesla Quarterly Revenue" in str(table):
        tesla_table = table
        break

# Extraer los datos de la tabla
dates = []
revenues = []

rows = tesla_table.find_all("tr")

for row in rows[1:]:  # Saltar la fila del encabezado
    cols = row.find_all("td")
    if len(cols) == 2:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip().replace("$", "").replace(",", "")
        if revenue != "":
            dates.append(date)
            revenues.append(revenue)

# Crear el DataFrame
tesla_revenue = pd.DataFrame({
    "Date": dates,
    "Revenue": revenues
})

# Convertir a valores numéricos
tesla_revenue["Revenue"] = pd.to_numeric(tesla_revenue["Revenue"], errors="coerce")

# Mostrar las últimas 5 filas
print(tesla_revenue.tail())
