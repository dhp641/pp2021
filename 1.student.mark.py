#!/usr/bin/env python
# coding: utf-8

# In[2]:


class student:
    studentData=[]
    def number_of_student ():
        print ("Number of student:")
    
    def infor_of_student():
        print("Add student: ")
        infor={'student name':''
               'student id':''
               'student dob':''
        }
            print("Student id:")
            id = input()
 
        while True:
            student = self.findStudent(id)
            if student != False:
                print("This id already has been. New id:")
                id = input()
            else:
                break
 
        infor['id'] = id

        print("student name:")
        infor['student name'] = input()
        print("student dob:")
        infor['student dob'] = input()
    
        self.listStudents.append(infor)


# In[3]:


class course:
    courseData=[]
    def number_of_course ():
        print ("Number of course:")
    
    def infor_of_course():
        print("Add course: ")
        infor={'course name':''
               'course id':''
        }
        print("Course id:")
            id = input()
 
        while True:
            course = self.findCourse(id)
            if student != False:
                print("This id already has been. New id:")
                id = input()
            else:
                break
 
        infor['id'] = id

        print("Course name:")
        infor['course name'] = input()
    
        self.listCourses.append(infor)


# In[5]:


def select_course(course_name):
    for i in range (len(course_name)):
        print("{i}, {course_name[i]}")
    no_course = int(input("ID of the course: "))
    return no_course

class mark_sheet:
    def create_mark_sheet(number_course, number_student):
        mark_sheet = [[0 for i in range(number_student)] for j in range(number_course)]
        return mark_sheet
    def mark_course(course_name, student_name, mark_sheet)
        no_course = select_course(course_name)
        for i in range (mark_sheet[no_course]):
            mark = float(input("mark of student[i]: "))
            mark_sheet[no_course][i] = mark


# In[4]:


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
        


# In[ ]:




