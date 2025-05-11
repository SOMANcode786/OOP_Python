# 👇 Class banai gai hai jo student ka structure define karti hai
class student:
    '''A class representing a student.'''

# 👇 ya constructor ha (__init__) class ka object banate waqt call hota hai
    def __init__(self,name,age,rollno):
        '''Initialize the student with name, age, and roll number.'''
        self.name = name
        self.age = age
        self.rollno = rollno


    def display(self):
        '''Display the student's information.'''
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll No: {self.rollno}")

student1=student("Ali", 20, 101)
student1.display()