class Person:

    def print_info(self):
        print(self.name,"is", self.age)

    def anotherFunc(self):
        pass

class Animal:
    def __init__(self, name, age = 1):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name,"is", self.age)

john = Person()
john.name = "John"
john.age = 22

lucy = Person()
lucy.name = "Lucy"
lucy.age = 21

Person.print_info(john)
john.print_info()

cat1 = Animal("Bursic")
cat1.print_info()
