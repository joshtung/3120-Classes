class Animal:
    def __init__(self, name, animal, energy=30):
        self.__name = name
        self.__animal = animal
        self.__energy = energy
        print(f"Hi, my name is {self.__name} and I am a {self.__animal}!")

    def talk(self):
        print(f"{self.__name} is snoring.")

    def sleep(self):
        self.__energy += 70
        print(f"{self.__name} is sleeping. Current energy level: {self.__energy}/100")

    def run(self):
        self.__energy -= 25
        print(f"{self.__name} is running. Energy level: {self.__energy}/100")

    def jump (self):
        self.__energy -= 45
        print(f"{self.__name} is jumping. Energy level: {self.__energy}/100")

    def eat(self):
        self.__energy += 60
        print(f"{self.__name} is eating. New energy level: {self.__energy}/100")

    def drink(self):
        self.__energy += 10
        print(f"{self.__name} is drinking coffee. {self.__name} is now {self.__energy}/100 full of ernergy.")