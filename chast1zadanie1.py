import pandas as pd

# скачка данных в DataFrame с ссылки которую давали откуда брать ксв
url = "https://www.geos.ed.ac.uk/~weather/jcmb_ws/JCMB_2015_May.csv"
data = pd.read_csv(url)

print(data.head())


'''
import pandas as pd

url = "https://www.geos.ed.ac.uk/~weather/jcmb_ws/JCMB_2006.csv"
data = pd.read_csv(url)
print(data.head())

#пример так же еще на 2006 год весит 19,5 мб
'''