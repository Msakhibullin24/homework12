import pandas as pd
import matplotlib.pyplot as plt

saved_data = pd.read_csv("first_1000_rows.csv")
saved_data.columns = saved_data.columns.str.strip() # Удаляем лишние пробелы из названий столбцов

saved_data['date-time'] = pd.to_datetime(saved_data['date-time'], errors='coerce')   # Преобразуем столбец даты в формат datetime

top_10_windspeed = saved_data.nlargest(10, "wind speed (m/s)") # Находим 10 самых больших значений скорости ветра
top_10_windspeed.plot(
    kind="bar",
    x="date-time",  #
    y="wind speed (m/s)",
    color="blue",
    figsize=(10, 6),
    title="Top-10 значений скорости ветра (м/с)"
)

plt.show()

'''
import pandas as pd
import matplotlib.pyplot as plt

saved_data = pd.read_csv("first_1000_rows.csv")
saved_data.columns = saved_data.columns.str.strip()   # Удаляем лишние пробелы из названий столбцов
saved_data['date-time'] = pd.to_datetime(saved_data['date-time'], errors='coerce')  # Преобразуем столбец даты в формат datetime

filtered_data = saved_data[saved_data['date-time'].dt.year > 2017]
top_10_windspeed = filtered_data.nlargest(10, "wind speed (m/s)") # Находим 10 самых больших значений скорости ветра


print(top_10_windspeed)

plt.figure(figsize=(10, 6))
plt.bar(top_10_windspeed.index, top_10_windspeed["wind speed (m/s)"], color='blue')
plt.title("Top-10 значений скорости ветра (м/с), старше 2017 года", fontsize=16)
plt.xlabel("Индексы строк", fontsize=12)
plt.ylabel("Скорость ветра (м/с)", fontsize=12)
plt.grid(alpha=0.3)
plt.show()
'''