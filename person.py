class Person:
    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age

    def showMsg(self):
        print(f'Jmenuji se {self.name} {self.surname} a je mi {self.age}')

clovek1 = Person('Pavel', 'Novak', 45)
clovek1.showMsg()


class Student(Person):
    #spec = 'devOps'
    def __init__(self, name, surname, age, spec):
        super().__init__(name, surname, age)
        self.spec=spec

    def showMsg(self):
        return (f'{super().showMsg()} a specializace je {self.spec}')

student1 = Student('Adam', 'Vesely', 45, 'HW')
print(student1.spec)
print(student1.showMsg())
print(clovek1.showMsg())


