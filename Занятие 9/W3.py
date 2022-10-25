class Car:
    def __init__(self, Color, Name, km):
        self.Color = Color
        self.Name = Name
        self.km = km
        lst = [Color, Name, km]
        print(lst)

    def Running(self):
        self.km += int(input("km "))
        print(self.km, self.Color, self.Name)


car1 = Car("color1", "car1", 0)
car2 = Car("color2", "car2", 0)
car3 = Car("color3", "car3", 0)


car1.Running()
car2.Running()
car3.Running()