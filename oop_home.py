import random

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.__person_id = random.randint(1,100)

    def __get_id(self):
        return f"{self.__person_id}\n"

    def get_info(self):
        return f"{self.__get_id()} Person first name - {self.name}; last name - {self.surname}; age {self.age}."

    def get_hi(self, text_msg):
        person_hi = self.get_info()
        return f"{person_hi}\n{text_msg}! I am {self.name}."


person1 = Person("Joe", "Black", 30)
# print(person1.get_hi("Hi"))
# person1.age = 35
# print(person1.get_hi("Hi"))
# person1.__person_id = 100
# print(person1.get_info())


class Persson:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def getInfo(self):
        return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self.age}."

    def getHi(self, msgText):
        return f"{msgText}! I am {self.firstName}."


persson1=Persson("Joe","Black",30)
persson2=Persson("Kate","Smith",20)
print(persson1.getInfo())
print(persson2.getInfo())
print(persson1.getHi("Hi"))
print(persson2.getHi("Hello"))


class Student(Persson):
    spec="Computer Science"
    def isSuccessful(self,meanScore):
        return True if meanScore>=75 else False

student1=Student("Joe","Black",30)
print(student1.getInfo())
print(student1.getHi("Morning"))
print(f"Is {student1.firstName} successful student?.{student1.isSuccessful(85)}")
