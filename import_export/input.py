import pandas as pd
import numpy as np
import model.course as mc
import model.instructor as mi
import model.student as ms


class InputManager:

    def __init__(self, filename, time_slices_in_an_hour):
        self.filename = filename
        self.time_slices_in_an_hour = time_slices_in_an_hour
        self.time_slices = -1

    def process_instructors(self):
        instructors_sheet = pd.read_excel(self.filename, 'Instructors', header=None)
        number_of_rows = len(instructors_sheet)  # all rows, including the first 2 which don't contain useful data
        number_of_hours = len(instructors_sheet.iloc[0]) - 6
        self.time_slices = number_of_hours * self.time_slices_in_an_hour

        instructors = []
        # getting the data row-by-row
        for i in range(2, number_of_rows):
            row = instructors_sheet.iloc[i]
            name = row[0]

            roles = []
            for j in range(1, 6):
                if row[j] == 'X':
                    roles.append(True)
                else:
                    roles.append(False)

            availability = []   # time intervals, where the instructor is available. First time slice's index is 0.
            start_time = None
            for j in range(6, len(row)):
                if row[j] == 'X' and start_time is None:
                    start_time = (j - 6) * self.time_slices_in_an_hour   # -6 because of the offset, and 12 time slices in an hour
                elif row[j] != 'X' and start_time is not None:
                    current_time = (j - 6) * self.time_slices_in_an_hour
                    availability.append([start_time, current_time])
                    start_time = None
            if start_time is not None:      # the last interval's end
                end_time = (len(row) - 6) * self.time_slices_in_an_hour
                availability.append([start_time, end_time])

            instructors.append(mi.Instructor(name, roles, availability))
        return instructors

    def process_students(self):
        students_sheet = pd.read_excel(self.filename, 'Students')
        number_of_rows = len(students_sheet)  # all rows (Header not included)
        students = []
        for i in range(number_of_rows):
            row = students_sheet.iloc[i]
            name = row[0]
            neptun = row[1]
            degree = row[2]
            program = row[3]
            supervisor = row[4]
            exam_courses = [row[6]]
            if not pd.isna(row[8]):     # if not NaN
                exam_courses.append(row[8])

            students.append(ms.Student(name, neptun, degree, program, supervisor, exam_courses))
        return students

    def process_courses(self):
        courses_sheet = pd.read_excel(self.filename, 'Courses', header=None)
        number_of_columns = len(courses_sheet.columns)
        courses = []
        for i in range(number_of_columns):
            column = courses_sheet[i]
            course_id = column[0]
            instructors = []
            for j in range(2, len(column)):     # column[1] is not needed
                if pd.isna(column[j]):
                    break
                instructors.append(column[j])
            courses.append(mc.Course(course_id, instructors))
        return courses


"""
test = InputManager('../Input_teljesZV/input19_2020osz_2_output.xlsx', 12)
test.process_instructors()[0].tostring()
students_test = test.process_students()
for student in students_test:
    student.tostring()
"""
