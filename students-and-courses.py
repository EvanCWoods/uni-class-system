current_enrollment = 0

def add_enroll(num):
    num += 1

class Student:
    def __init__(self, fName, lName, age, degree, gpa):
        self.fName = fName
        self.lName = lName
        self.age = age
        self.degree = degree
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa

    def is_honors(self):
        if self.gpa > 3.6:
            return True
        else:
            return False


class Course:
    def __init__(self, title, enrolled, max_students):
        self.title = title
        self.enrolled = enrolled
        self.max_students = max_students

    def enroll(self):
        if current_enrollment < self.max_students:
            add_enroll(current_enrollment)

    def is_full(self):
        if self.enrolled == self.max_students:
            return True
        elif self.enrolled < self.max_students:
            return False



def main():
    course1 = Course('maa', 0, 13)
    print(course1.max_students)
    course1.enroll()
    print(course1.is_full())


if __name__=='__main__':
    main()
