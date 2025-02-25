class Animal:

    def __init__(self, name, stamina = 50, hunger = 50): 
        self.__name = name
        self.__stamina = stamina
        self.__hunger = hunger
        print("hello, I am", self.__name)
        
    def run(self):
        self.__stamina -= 10
        self.__hunger -= 10
        print("Whew, I am hungry and tired now.")
        print(f"I have {self.__hunger} hunger and {self.__stamina} stamina now.")
      
    def talk(self,sound):
        self.__sound=sound
        print(f"{self.__sound}")

    def eat(self): 
        self.__hunger += 20
        print("burp")
        print(f"I have {self.__hunger} hunger now.")

    def sleep(self):
        self.__stamina += 50
        print("I am full of energy now")
        print(f"I have {self.__stamina} stamina now.")

    def play(self):
        self.__stamina -= 10
        print("That was fun")

    def drink(self):
        self.__hunger += 5 
        print("Refreshing")



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