import string
import math

def max_digit(x):
    res = 0
    for item in x:
        if item > res:
            res = item
    return res

def concatenation(a, b, string):
    return string.format(a, b, a + b)

def rectangle(height, width):
    print("*" * width)
    for i in range(height -2):
        print('*', ' ' * (width - 2), '*', sep = '')
    print('*' * width)

def serching_digit(a, _list):
    res = -1
    for item in _list:
        if a == item:
            res = _list.index(a)
    return res

def count_word(text):
    res = {}
    for item in string.punctuation:
        text = text.replace(item, "")
    text = text.split()
    for item in text:
        if not res.get(item):
            res[item] = text.count(item)
    return res

def subsequence(x):
    res = 0
    if x[1] - x[0] == x[2] - x[1]:
        res = x[0] + (x[1] - x[0]) * len(x)
        return res
    elif x[1] / x[0] == x[2] / x[1]:
        res = x[0] * (x[1] // x[0]) ** len(x)
        return res
    elif math.log(x[1], 2) == math.log(x[2], 3):
        res = int((x[len(x) - 1] ** (1 / math.log(x[1], 2)) + 1) ** math.log(x[1], 2))
        return res
    else:
        return None


    

if __name__ == '__main__':
    print("Exercise 1:")
    x = [1, 8, 4, 7, 9, 30, 11, 3, 28]
    print("Список чисел:", x)
    print("Максимальное число в списке:", max_digit(x))

    print("\nExercise 2:")
    a = 4
    b = 24
    str = "Первое число: {0}, второе число: {1}, сумма: {2}"
    print(concatenation(a, b, str))

    print("\nExercise 3:")
    height = 5
    width = 4
    rectangle(5, 4)

    print("\nExercise 4:")
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Список:", x)
    a = 5
    b = 11
    if serching_digit(a, x) != -1:
        print(f"Индекс числа {a}: {serching_digit(a, x)}")
    else:
        print("Числа", a, "нету в списке")

    if serching_digit(b, x) != -1:
        print(f"Индекс числа {b}: {serching_digit(b, x)}")
    else:
        print("Числа", b, "нету в списке")

    print("\nExercise 5:")
    text = "Hello world! Hello Ivan! Ivan like Python. Ivan writting first program!"
    print("Количество слов в тексте:", count_word(text))

    print("\nExtra Exercise 1:")
    x = input("Введите последовательность: ")
    x = x.split()
    x = list(map(int, x))
    if subsequence(x):
        print("Следующий элемент последовательности:", subsequence(x))
    else:
        print("Невозможно высчитать следующий элемент последовательности!")
    