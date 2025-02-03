import pandas as pd
import numpy as np

#Q2: Из получившихся данных выбрать данные по
index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020]
    ],
    names=['city', 'year']
)

columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)

rng = np.random.default_rng(1)
data = rng.random((4, 6))

data_df = pd.DataFrame(data, index=index, columns=columns)

#    2020 году (для всех столбцов)
data_2020 = data_df.xs(2020, level='year')
print(data_2020)

#    job_1 (для всех строк)
data_job_1 = data_df.xs('job_1', axis=1, level='job')
print(data_job_1)

#    для city_1 и job_2
data_city_1 = data_df.xs('city_1', level='city')
result = data_city_1.xs('job_2', axis=1, level='job')
print(result)

#Q3: Взять за основу DataFrame со следующей структурой:
index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020]
    ],
    names=['city', 'year']
)
columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)
df = pd.DataFrame(data, index=index, columns=columns)

# Выполнить запрос на получение следующих данных
# - все данные по person_1 и person_3
data_person_1 = df.xs('person_1', level='worker', axis=1)
data_person_3 = df.xs('person_3', level='worker', axis=1)
data_persons_13 = pd.concat([data_person_1, data_person_3], axis=1)
print(data_persons_13)

# - все данные по первому городу и первым двум person-ам (с использование срезов)
first_city = df.xs('city_1', level='city', drop_level=False)
first_two_persons = first_city[['person_1', 'person_3']]
print(first_two_persons)

# Приведите пример (самостоятельно) с использованием pd.IndexSlice
idx = pd.IndexSlice
selected_data = df.loc[idx['city_1', :], idx[['person_1', 'person_2'], :]]
print(selected_data)

#Q4: Привести пример использования inner и outer джойнов
# для Series (данные примера скорее всего нужно изменить)???
ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
ser2 = pd.Series(['b', 'c', 'f'], index=[4,5,6])

print (pd.concat([ser1, ser2], join='outer'))
print (pd.concat([ser1, ser2], join='inner'))

