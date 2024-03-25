#Question 3

def ave_grade(grades):#Task 1
    average= float(sum(grades)/len(grades))
    print(average)
def min_and_max(grades):#Task 2
    lowest_grade = min(grades)
    highest_grade = max(grades)
    print(f"The lowest grade is: {lowest_grade} and the highest grade is: {highest_grade}")

    
student_grades =[100, 52, 65 ,70 ,60, 80, 90, 55]

ave_grade(student_grades)
min_and_max(student_grades)

def grade_book(grades):#Task 3
    for grade in grades:
        if 0 <= grade  <= 59:
            grades[grades.index(grade)]='F'
        elif grade <=69:
            grades[grades.index(grade)]='D'
        elif grade <=79:
            grades[grades.index(grade)]='C'
        elif grade <=89:
            grades[grades.index(grade)]='B'
        elif grade <= 100:
            grades[grades.index(grade)]='A'
        else:
            grades[grades.index(grade)]="Grade is not valid."
    print(f"New letters grades are: {grades}")

grade_book(student_grades)
