#запрашиваем возраст пользователя
age = float(input("age: "))
#выводим сообщение об ошибке, если было введено отрицательное число
if age < 0:
    print("error, negative number")
#рассчитываем и выводим возраст собаки
if age >= 0 and age < 10.5:
    print("dog age: 0")
elif age >= 10.5 and age < 21:
    print("dog age: 1")
elif age >= 21 and age < 25:
    print("dog age: 2")
elif age >= 25:
    print("dog age:", 2 + (age - 21)/4)
