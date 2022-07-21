from distutils.archive_util import make_archive


class Vehicle:
    wheels=4
    def __init__(self,make,model,nick_name,year):
        self.model = model.capitalize()
        self.make = make.capitalize()
        self.nick_name = nick_name.capitalize()
        self.year = year
    
    def __str__(self) -> str:
            return(f"{self.nick_name} is a {self.year} {self.make} {self.model}!")

    def drive(self, speed):
        if speed > 60:
            print("You're going really fast!")
        else:
            print("you drive really slow")

class Motorcycle(Vehicle):
    wheels = 2


sid = Vehicle("tesla","model3","sid","2022")
print(sid,sid.wheels)
sid.drive(75)
harley=Motorcycle("Harley","davidson","demon",1990)
print(harley)
harley.drive(45)

