
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_info(self):
        return f"Person first name - {self.name}; last name - {self.surname}; age {self.age}."

    def get_hi(self, text_msg):
        person_hi = self.get_info()
        return f"{person_hi}\n{text_msg}! I am {self.name}."


person1 = Person("Joe", "Black", 30)
print(person1.get_hi("Hi"))
person1.age = 35
print(person1.get_hi("Hi"))