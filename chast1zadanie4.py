import pandas as pd

# теперь закидываем файл ферст100роулс чтобы они могли подкачаться и мы от туда финфу могли вытащить
saved_data = pd.read_csv("first_1000_rows.csv")

# ну тут опираемся на хед 24
print(saved_data.head(24))
# Показываем ласт 24
print(saved_data.tail(24))
# тут срез показываем и цифры диапазон их
print(saved_data[11:24])
