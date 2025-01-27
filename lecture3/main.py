import numpy as np
import pandas as pd

#Q1: Привести различные способы создания объектов типа Series
#Через списки Python
data = [10, 20, 30]
series = pd.Series(data)
print(series)

#Через массивы NumPy
array = np.array([50, 60, 70])
series = pd.Series(array)
print(series)

#Через скалярные значение
scalar_value = 42
size = 5
series = pd.Series(scalar_value, index=range(size))
print(series)

#Через словарь
dictionary = {'apple': 4, 'banana': 6, 'cherry': 8}
series = pd.Series(dictionary)
print(series)


#Q2: Привести различные способы создания объектов типа DataFrame
#Через серии
names = pd.Series(["Alice", "Bob", "Charlie"], name="Name")
ages = pd.Series([25, 32, 28], name="Age")
df = pd.concat([names, ages], axis=1)
print(df)

#Через список словарей
data = [
    {"Name": "Alice", "Age": 25},
    {"Name": "Bob", "Age": 32},
    {"Name": "Charlie", "Age": 28}
]
df = pd.DataFrame(data)
print(df)

#Через словарь серий
names = pd.Series(["Alice", "Bob", "Charlie"])
ages = pd.Series([25, 32, 28])
dict_of_series = {"Name": names, "Age": ages}
df = pd.concat(dict_of_series, axis=1)
print(df)

#Через двумерный массив NumPy
data = np.array([
    ["Alice", 25],
    ["Bob", 32],
    ["Charlie", 28]
])
df = pd.DataFrame(data=data, columns=["Name", "Age"])
print(df)

#Через структурированный массив NumPy
dtype = [('Name', 'U10'), ('Age', 'i4')]
data = np.array(
    [('Alice', 25), ('Bob', 32), ('Charlie', 28)],
    dtype=dtype
)
df = pd.DataFrame(data)
print(df)


#Q3: Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так,
#    чтобы вместо NaN было установлено значение 1
s1 = pd.Series({'a': 10, 'b': 20, 'c': 30})
s2 = pd.Series({'d': 40, 'e': 50, 'f': 60})
result = s1.add(s2, fill_value=1)
print(result)


#Q4: Переписать пример с транслирование для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ
rng = np.random.default_rng(1)

A = rng.integers(0, 10, (3, 3))
print(A)
column = A[:, 0]
print(column)
result = A.T - column
print(result.T)


#Q5: На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()
data = {
    'A': [1, np.nan, 3, np.nan, 5],
    'B': [np.nan, 2, np.nan, 4, np.nan],
    'C': [np.nan, np.nan, np.nan, 6, 7]
}
df = pd.DataFrame(data)
print("Исходный DataFrame:")
print(df)
df_ffilled = df.ffill()
print("\nDataFrame после ffill():")
print(df_ffilled)
df_bfilled = df.bfill()
print("\nDataFrame после bfill():")
print(df_bfilled)