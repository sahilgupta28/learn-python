class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello {self.name}!")


name = input('Your name: ')
person1 = Person(name)

person1.talk()