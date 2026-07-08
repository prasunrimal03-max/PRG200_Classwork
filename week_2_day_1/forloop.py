names = []
marks = []

for i in range(20):
    name = input("Enter student name: ")
    mark = float(input("Enter marks: "))

    names.append(name)
    marks.append(mark)

for i in range(20):
    if marks[i] >= 80:
        print(names[i], "-", "Distinction")
    elif marks[i] >= 60:
        print(names[i], "-", "First Division")
    elif marks[i] >= 45:
        print(names[i], "-", "Second Division")
    elif marks[i] >= 32:
        print(names[i], "-", "Third Division")
    else:
        print(names[i], "-", "Fail")