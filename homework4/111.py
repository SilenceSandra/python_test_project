#Задание 1
#Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов.
# Учитываем, что может быть повторяющиеся значения аргументов.

def min_second(*args):
    empty = []
    largs = list(args)
    for element in largs:
        if not (element in empty):
            empty.append(element)
        empty.sort()
    return empty[1]

