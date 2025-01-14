## 1. Какие еще существуют коды типов?
## 'b' - signed char
## 'B' - unsigned char
## 'u' - wchar_t
## 'w' - Py_UCS4
## 'h' - signed short
## 'H' - unsigned short
## 'i' - signed int
## 'I' - unsigned int
## 'l' - signed long
## 'L' - unsigned long
## 'q' - signed long long
## 'Q' - unsigned long long
## 'f' - float
## 'd' - double

## 2. Напишите код, подобный приведенному выше, но с другим типом
import array
import sys
a1 = array.array('d', [1.0, 2.0, 3.0])
print(sys.getsizeof(a1))
print(type(a1))

## 3. Напишите код для создания массива с 5 значениями,
##    располагающимися через равные интервалы в диапазоне от 0 до 1
import numpy as np
array = np.linspace(0, 1, num=5)
print(array)

## 4. Напишите код для создания массива с 5 равномерно
##    распределенными случайными значениями в диапазоне от 0 до 1
random_array = np.random.uniform(0, 1, size=5)
print(random_array)

## 5. Напишите код для создания массива с 5 нормально
##    распределенными случайными значениями с мат. ожиданием = 0 и дисперсией 1
normal_array = np.random.normal(loc=0, scale=1, size=5)
print(normal_array)

## 6. Напишите код для создания массива с 5 случайнвми целыми числами в от [0, 10)
random_integers = np.random.randint(0, 10, size=5)
print(random_integers)

## 7. Написать код для создания срезов массива 3 на 4
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
## - первые две строки и три столбца
sliced_arr = arr[:2, :3]
print([sliced_arr])
## - первые три строки и второй столбец
sliced_arr = arr[:3, 1]
print([sliced_arr])
## - все строки и столбцы в обратном порядке
sliced_arr = arr[::-1, ::-1]
print([sliced_arr])
## - второй столбец
sliced_arr = arr[:, 1]
print([sliced_arr])
## - третья строка
sliced_arr = arr[2, :]
print([sliced_arr])

## 8. Продемонстрируйте, как сделать срез-копию
sliced_arr = arr[::-1, ::-1].copy()
sliced_arr[0, 0] = 100
print(arr)
print(sliced_arr)

## 9. Продемонстрируйте использование newaxis для получения вектора-столбца и вектора-строки
arr = np.array([1, 2, 3])
vector_stroka = arr[np.newaxis, :]
print("вектор строка:", vector_stroka)
print("Shape:", vector_stroka.shape)

vector_stolbec = arr[:, np.newaxis]
print("Vector-column:", vector_stolbec)
print("Shape of column vector:", vector_stolbec.shape)

## 10. Разберитесь, как работает метод dstack
## dstack принимает список массивов и объединяет их вдоль новой оси,
## которая добавляется как третье измерение.
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
result = np.dstack((arr1, arr2))
print(result)

## 11. Разберитесь, как работают методы split, vsplit, hsplit, dsplit
## Метод split разбивает массив на указанное число частей вдоль указанной оси.
arr = np.arange(16).reshape(4, 4)
parts = np.split(arr, 2, axis=0)
print(parts)
## Метод vsplit разбивает массив на указанное число частей вдоль вертикальной оси (оси 0).
arr = np.arange(16).reshape(4, 4)
parts = np.vsplit(arr, 2)
print(parts)
## Метод hsplit разбивает массив на указанное число частей вдоль горизонтальной оси (оси 1).
arr = np.arange(16).reshape(4, 4)
parts = np.hsplit(arr, 2)
print(parts)
## Метод dsplit разбивает массив на указанное число частей вдоль глубины (третья ось).
arr = np.arange(24).reshape(2, 3, 4)
parts = np.dsplit(arr, 2)
print(parts)
## 12. Привести пример использования всех универсальных функций, которые я привел
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
## +
c = np.add(a, b)
print(c)
## -
c = np.subtract(b, a)
print(c)
## *
c = np.multiply(a, b)
print(c)
## /
c = np.divide(b, a)
print(c)
## %
c = np.remainder(a, b)
print(c)
## //
c = np.floor_divide(a, b)
print(c)
## **
c = np.power(a, 2)
print(c)
## sin
c = np.sin(np.pi / 2)
print(c)
## cos
c = np.cos(np.pi)
print(c)
## tg
c = np.tan(np.pi / 4)
print(c)
## exp
c = np.exp(1)
print(c)
## ln
c = np.log(2.71828)
print(c)
## sinh
c = np.sinh(c)
print(c)
## cosh
c = np.cosh(c)
print(c)
