summ = float(input("Сумма заказа: ")) #ввод с клавиатуры суммы заказа
tax = summ*0.20 #вычисляем налог
tips = summ*0.18 #вычисляем сумму чаевых
result = summ + tax + tips #вычисляем итог
print("Налог: ", "%.2f" %tax) #вывод налога
print("Чаевые: ", "%.2f" %tips) #вывод чаевых
print("Итог: ", "%.2f" %result) #вывод результата
