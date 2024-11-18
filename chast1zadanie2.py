import pandas as pd

url = "https://www.geos.ed.ac.uk/~weather/jcmb_ws/JCMB_2015_May.csv"
data = pd.read_csv(url)
# Список всех столбцов
print(data.columns)

# Если нужно переименовать столбцы то их можно переименвать так как снизу в коде
#data.rename(columns={"Rel Hum (%)": "relativehumidity (%)", "Wind Spd (m/s)": "windspeed (m/s)"}, inplace=True)
