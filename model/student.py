class Student:

    def __init__(self, name, neptun, degree_level, program, supervisor, exam_courses, ):
        self.name = name
        self.neptun = neptun
        self.degree_level = degree_level
        self.program = program
        self.supervisor = supervisor
        self.exam_courses = exam_courses    # list of course codes (course names are unnecessary)
        self.number_of_exams = len(exam_courses)

    def tostring(self):
        print(self.name)
        print('Neptun: ', self.neptun)
        print('Degree level: ', self.degree_level)
        print('Program: ', self.program)
        print('Supervisor: ', self.supervisor)
        print('Number of exams: ', self.number_of_exams)
        print('Exam courses:')
        for course in self.exam_courses:
            print('\t', course)