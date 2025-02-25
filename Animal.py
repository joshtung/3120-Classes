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
        

