class Dog:
    def __init__(self,name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof")

dax = Dog("Dax")
buster = Dog("Buster")

dax.bark()
buster.bark()