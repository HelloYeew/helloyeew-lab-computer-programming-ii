class Pet():

    def __init__(self, name, owner):
        self.is_alive = True  # It's alive!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)


class Dog(Pet):

    def talk(self):
        print(self.name + ' says woof!')


class Cat(Pet):

    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
        self.lives = lives

    def talk(self):
        print(self.name + " say meow!")

    def lose_life(self):
        if self.lives == 0:
            print("No more lives to lose!")
        else:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False


class NoisyCat(Cat):

    def talk(self):
        super().talk()
        print(self.name + " say meow!")

