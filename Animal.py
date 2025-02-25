class Animal:
    def __init__(self, name, stamina = 50, hunger = 50): 
        self.__name = name
        self.__stamina = stamina
        self.__hunger = hunger
        print("hello, I am", self.__name)

    def talk(self):
        print("hi")

    def run(self):
        self.__stamina -= 10
        self.__hunger -= 10
        print("Whew, I am hungry and tired now.")
        print(f"I have {self.__hunger} hunger and {self.__stamina} stamina now.")

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



