import matplotlib.pyplot as plt
import pandas as pd

saved_data = pd.read_csv("first_1000_rows.csv")

# Топ-10 значений
top_10_windspeed = saved_data.nlargest(10, "windspeed (m/s)")

# Построение графика
plt.figure(figsize=(10, 6))
plt.bar(top_10_windspeed.index, top_10_windspeed["windspeed (m/s)"], color='blue')
plt.title("Топ-10 значений скорости ветра", fontsize=16)
plt.xlabel("Индексы строк", fontsize=12)
plt.ylabel("Скорость ветра (м/с)", fontsize=12)
plt.grid(alpha=0.3)
plt.show()

#ff