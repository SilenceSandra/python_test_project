a = input()
if len(a) < 5:
   print ("Строка слишком короткая!")
else:
   print(a[2], a[-2], a[:5], a[:-2], a[0:len(a):2], a[1:len(a):2], a[::-1], a[::-2], len(a),sep = "\n" )