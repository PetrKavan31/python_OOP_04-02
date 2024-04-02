class Person:
    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age

    def showMsg(self):
        print(f'Jmenuji se {self.name} {self.surname} a je mi {self.age}')

clovek1 = Person('Pavel', 'Novak', 45)
clovek1.showMsg()