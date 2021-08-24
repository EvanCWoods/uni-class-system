students_list = []

class Student:
    def __init__(self, fName, lName, course, gpa):
        self.fName = fName
        self.lName = lName
        self.course = course
        self.gpa = gpa

    def is_honours(self):
        if self.gpa < 3.6:
            print(f'{self.fName} ' + f' {self.lName} ' + 'Does not have honours')
        else:
            print(f'{self.fName}' + f'{self.lName} ' + 'Does have honours')


def create_student():
    fName = input('Enter your first name: ')
    lName = input('Enter your last name: ')
    course = input('Enter your course/degree: ')
    gpa = float(input('Enter your GPA: '))
    
    students_list.append(Student(fName, lName, course, gpa))


def main():
    student1 = Student('Evan', 'Woods', 'Commerce', 3)
    print(student1.is_honours())
    create_student()
    print(students_list[0].gpa)
    print(students_list[0].is_honours())
    

if __name__=='__main__':
    main()   