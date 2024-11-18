import pandas as pd

# Чтение данных из файла
saved_data = pd.read_csv("first_1000_rows.csv")

# Проверка названий столбцов
print(saved_data.columns)

# Удаление пробелов из названий
saved_data.columns = saved_data.columns.str.strip()

# Подсчет уникальных значений
unique_count = saved_data["Rel Hum (%)"].nunique()  # или правильное имя
total_count = len(saved_data)
percentage_unique = (unique_count / total_count) * 100

print(f"Уникальных значений: {unique_count}")
print(f"Процент уникальных значений: {percentage_unique:.2f}%")


#ff