import pandas as pd

saved_data = pd.read_csv("first_1000_rows.csv") # по стандарту вставляем что имеем

# Удаление пробелов из названий
saved_data.columns = saved_data.columns.str.strip()
# Подсчет уникальных значений
unique_count = saved_data["relative humidity (%)"].nunique()
total_count = len(saved_data)
percentage_unique = (unique_count / total_count) * 100

print(f"Уникальных значений {unique_count}")
print(f"Процент уникальных значений {percentage_unique:.2f}%")
'''
import pandas as pd

saved_data = pd.read_csv("first_1000_rows.csv")     # база сохранненая мы из нее вытаскиваем данные 
saved_data["date-time"] = pd.to_datetime(saved_data["date-time"])   # Преобразуем столбец date-time в формат datetime
filtered_data = saved_data[saved_data["date-time"].dt.year > 2017]    # Фильтрация данных старше 2017 года у нас тут по 0 будет тк у нас данные 2015 годаа)
unique_count_filtered = filtered_data["relative humidity (%)"].nunique()    # Количество уникальных значений в столбце `relative humidity (%)` для отфильтрованных данных
total_count_filtered = len(filtered_data)   # Общее количество строк в отфильтрованных данных
# иф элс на выялвеение поцента уникальных значений
if total_count_filtered > 0:
    percentage_unique_filtered = (unique_count_filtered / total_count_filtered) * 100
else:
    percentage_unique_filtered = 0

print(f"Уникальных значений (для данных после 2017 года): {unique_count_filtered}")
print(f"Процент уникальных значений: {percentage_unique_filtered:.2f}%")

'''