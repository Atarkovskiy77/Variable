# Вводные данные к дополнительному заданию
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Первый вариант решения
a_1 = sum([5,3,3,5,4])/5
b_2 = sum([2, 2, 2, 3])/4
j_3 = sum([4, 5, 5, 2])/4
k_4= sum([4, 4, 3])/3
s_5 = sum([5, 5, 5, 4, 5])/5
students_average_score = {'Aaron': a_1 , 'Bilbo': b_2, 'Johnny': j_3,'Khendrik': k_4, 'Steve': s_5}
print(students_average_score )

# Второй вариант решения
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()
average_grades = (
    sum(grades[0]) / len(grades[0]),
    sum(grades[1]) / len(grades[1]),
    sum(grades[2]) / len(grades[2]),
    sum(grades[3]) / len(grades[3]),
    sum(grades[4]) / len(grades[4])
)
students_avg_grade = dict(zip(students_list, average_grades))
print(students_avg_grade)
