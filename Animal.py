class Animal:
    def __init__(self, name, skin, run):
        self.__name = name 
        self.__skin = skin
        self.__run = run
        print("hello, I am", self.__name)

    def talk(self):
        print(f"I talk like a {self.__name}")

    def color(self):
        print(f"My skin color is {self.__skin}")

    def run(self):
        print(f"I run very {self.__run}")
        

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



