import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL de la página
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"

# Simular que somos un navegador (user-agent)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Hacer la solicitud con headers
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Buscar todas las tablas
tables = soup.find_all("table")

# Buscar la tabla correcta
for table in tables:
    if "GameStop Quarterly Revenue" in str(table):
        gme_table = table
        break

# Extraer los datos
dates = []
revenues = []

rows = gme_table.find_all("tr")

for row in rows[1:]:
    cols = row.find_all("td")
    if len(cols) == 2:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip().replace("$", "").replace(",", "")
        if revenue != "":
            dates.append(date)
            revenues.append(revenue)

# Crear DataFrame
gme_revenue = pd.DataFrame({
    "Date": dates,
    "Revenue": revenues
})

# Convertir a números
gme_revenue["Revenue"] = pd.to_numeric(gme_revenue["Revenue"], errors="coerce")

# Mostrar últimas 5 filas
print(gme_revenue.tail())
