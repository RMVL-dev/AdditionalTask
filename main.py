grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

studentsAlphabet = sorted(students)
classJournal = {}
averageGrades = []

for grade in grades:
    averageGrades.append(sum(grade)/len(grade))

for position in range(len(studentsAlphabet)):
    classJournal[studentsAlphabet[position]] = averageGrades[position]

print(classJournal)
