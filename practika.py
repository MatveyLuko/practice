from statistics import mean
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades = [mean([5, 3, 3, 5, 4]), mean([2, 2, 2, 3]), mean([4, 5, 5, 2]), mean([4, 4, 3]), mean([5, 5, 5, 4, 5])]
for index, value in enumerate(grades):
    grades[index] = float(value)

students = sorted(students)

zipped = zip(students, grades)
students_grades = dict(zipped)

print(students_grades)



