# Записываем переменные
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
# Пишем условную конструкцию
if first == second == third:
    print ('Вывод: 3')
elif first == second or second == third or first == third:
    print ('Вывод: 2')
else:
    print ('Вывод: 0')
# Проверяем результат