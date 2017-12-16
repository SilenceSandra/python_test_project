#Задание 5
#Создайте строку, в которой написан, какой-то текст. Пример:
#We are not what we should be!
#We are not what we need to be.
#But at least we are not what we used to be
# (Football Coach)
#Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
#Удалите знаки препинания (пройдитесь циклом все слова и удалите методом strip знаки препинания)
#Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)

s = "We are not what we should be!\nWe are not what we need to be.\nBut at least we are not what we used to be\n  (Football Coach)"
s2 = s.split( )
print(s2)
print(len(s.split( )))
print(len(s2))
for i in s2:
    print(i.strip(".!()"))




