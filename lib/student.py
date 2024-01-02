#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
    
    def learn(self, phrase):
        self.knowledge.append(phrase)
         
# student = Student("ana", "cole")
# test = student.learn("eu sou a ana")
# print(test) put a return before the last line of code
#print(Student.__bases__)
        