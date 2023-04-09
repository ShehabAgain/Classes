class PlayerCharacter:
    membership = True  # Class Object Attribute; not dynamic

    def __init__(self, name, age):
        if (age >= 18):
            self.name = name  # attributes which the Characters possess
            self.age = age

    def shout(self):
        print(f"my name is {self.name}")

    def run(self, hello):
        print(f"my name is {self.name} and i am {hello}")

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1+num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1+num2


player1 = PlayerCharacter('Cindy', 19)
print(player1.membership)
player3 = PlayerCharacter.adding_things(2, 3)
print(player1.shout())
print(player3)
print(player1.run("cool"))
