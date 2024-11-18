import numpy as np

mean = 0  # математическое ожидание
variance = 5  # дисперсия
std_dev = np.sqrt(variance)  # стандартное отклонение

random_vector = np.random.normal(mean, std_dev, 2000) # Формирование вектора из 2000 случайных величин

# Вычисление экспериментального математического ожидания и дисперсии
experimental_mean = np.mean(random_vector)
experimental_variance = np.var(random_vector)

print("Экспериментальное математическое ожидание (среднеезначение значение):", experimental_mean)
print("Экспериментальная дисперсия:", experimental_variance)