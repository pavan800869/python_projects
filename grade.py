# to display grade of student

g = int(input("Enter the grade of the student: "))

if g> 90:
    grade = 'O'
elif g>80:
    grade ='A'
elif g>70:
    grade = 'B'
elif g>60:
    grade = 'C'
elif g>50:
    grade = 'D'
elif g<=50:
    grade = 'F'

print(grade)
    
