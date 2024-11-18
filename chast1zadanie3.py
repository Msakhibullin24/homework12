import pandas as pd

url = "https://www.geos.ed.ac.uk/~weather/jcmb_ws/JCMB_2015_May.csv"
data = pd.read_csv(url)

data.head(1000).to_csv("first_1000_rows.csv", index=False)

print(data.head)