class Course:

    def __init__(self, id, insturctors):
        self.id = id
        self.instructors = insturctors

    def tostring(self):
        print(self.id)
        for instructor in self.instructors:
            print('\t', instructor)