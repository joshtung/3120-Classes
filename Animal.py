class Animal:
    def __init__(self, name, species, energy=100): 
        self.__name = name
        self.__species = species
        self.__energy = energy
        print("Hello, I am", self.__name, "and I am a", self.__species)
        print("Energy level:", self.__energy)

    def talk(self,sound):
        self.__sound=sound
        print(f"{self.__sound}")

    def love(self, thing1, thing2):
        self.__thing1= thing1
        self.__thing2=thing2
        print(f"{self.__name} loves {self.__thing1} and {self.__thing2}")

    def play(self):
        self.__energy -= 45
        print(f"{self.__name} plays happily")
        print("Energy level:", self.__energy)

    def food(self):
        print(f"{self.__name} eats lots of tasty food")
        self.__energy += 45
        print("Energy level:", self.__energy)





