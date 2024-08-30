# 2. Создать переменную immutable_var и присвоить ей кортеж из нескольких элементов разных типов данных
immutable_var = 1, 5.5, 'Andrey', True, 'gender'
# Выполнить операцию вывода кортежа immutable_var на экран
print(immutable_var)
# 3. Попытаться изменить элементы кортежа immutable_var
# immutable_var [3] = 100
# При выводе ответа выдаётся ошибка
# Ошибка буквально сообщает, что кортеж не поддерживает обращение по элементам
# То есть кортеж является неизменяемым списком
# 4. Создать изменяемую структуру данных
mutable_list =([1, 5.5, 'Andrey', True, 'gender'], 0)
print(mutable_list)
mutable_list [0][4] = 'male'
print(mutable_list)