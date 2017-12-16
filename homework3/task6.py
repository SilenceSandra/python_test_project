#Это уже было, но теперь оформите это функцией:
#Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
def is_year_leap (year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("True")
    else:
        print("False")


t = is_year_leap(2042)


#Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами.
# Если треугольник существует, вернёт True, иначе False.

def triang(a, b, c):
    if ((a + b) > c) and ((b + c) > a) and ((a + c) > b):
        print("True")
    else:
        print("False")


triang(2, 4, 5)