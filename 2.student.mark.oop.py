#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class student:
    infor_of_student = "name, id, dob"
    def __init__(self, studentName, studentId, studentDob):
        self.__studentName = studentName
        self.__studentId = studentId
        self.__studentDob = studentDob
    def get_studentName(self):
        return self.__studentName
    def get_studentID(self):
        return self.__studentID
    def get_studentDob(self):
        return self.__studentDob
    def set_student(self, studentName, studentID, studentDob):
        self.__studentName = studentName
        self.__studentId = studentId
        self.__studentDob = studentDob
    
        
class course:
    infor_of_course = "name, id"
    def __init__(self, courseName, courseId):
        self.__courseName = courseName
        self.__courseId = courseId
    def get_courseName(self):
        return self.__courseName
    def get_courseID(self):
        return self.__courseID
    def set_course(self, courseName, courseId):
        self.__courseName = courseName
        self.__courseId = courseId
    
class mark:
    def __init__(self, student, course, mark):
        self.__student =  student
        self.__course =  course
        self.__mark = mark
    def get_student(self):
        return self.__student
    def get_course(self):
        return self.__course
    def get_mark(self):
        return self.__mark
    def set_mark(self):
        self.__student =  student
        self.__course =  course
        self.__mark = mark

number_student = int(input("Number of student:"))
student[]
number_course = int(input("Number of course:"))
course[]

while True:
    action = int(input("Press 1: infor of student.\ Press 2: infor of course.\ Press 3: marking.\ Press 0: stop."))
    if action == 1:
        print_infor_of_student(name,id,dob)
    elif action == 2:
        print_infor_of_course(name,id)
    elif action == 3:
        print_mark(course_name, student_name, mark_sheet)
    else:
        break

        

    
    

