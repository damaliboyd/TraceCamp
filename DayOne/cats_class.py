# Parent class
class Cat:

    # Class attribute
    species = 'mammal'

    is_hungry = True

    is_walking = False

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def eat(self):
        is_hungry = False

    def walk(self):
        is_walking = True

# Child class (inherits from Dog class)
class ShortHair(Cat):
    def lick(self, speed):
        return "{} licks {}".format(self.name, speed)

# Child class (inherits from Dog class)
class LongHair(Cat):
    def lick(self, speed):
        return "{} licks {}".format(self.name, speed)
