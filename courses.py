course_list = []

class Course:
    def __init__(self, name, code, faculty, enrollment, max_enrollment):
        self.name = name
        self.code = code
        self.faculty = faculty
        self.enrollment = enrollment
        self.max_enrollment = max_enrollment

    
    def enroll(self):
        if self.enrollment < self.max_enrollment:
            self.enrollment = self.enrollment + 1
        elif self.enrollment == self.max_enrollment:
            print('This class is full. Enroll in another class.')
 

def create_course():
    name = input('Enter the name of the course: ')
    code = input('Enter the course code: ')
    faculty = input('Enter the faculty that this course belongs to: ')
    enrollment = int(0)
    max_enrollment = int(input('Enter the maximum number of students that can register for this course: '))

    course_list.append(Course(name, code, faculty, enrollment, max_enrollment))

def main():
    create_course()
    print(course_list[0].name)
    print(course_list[0].max_enrollment)
    for _ in range(15):
        course_list[0].enroll()
    print(course_list[0].enrollment)
 

if __name__=='__main__':
    main()