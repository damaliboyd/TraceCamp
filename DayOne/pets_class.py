from cats_class import Cat
# Parent class
class Pets:

    # Initializer
    def __init__(self):
        cat1 = Cat("Grandpa", 21);
        cat2 = Cat("Gatorade", 7);
        cat3 = Cat("Puppy", 1);

        self.pets_list = {
            cat1, cat2, cat3
        }
    # Instance Method
    def is_mammals(self):
        for pet in self.pets_list:
            if (pet.species != 'mammal'):
                return False
        return True

    def is_hunger(self):
        for pet in self.pets_list:
            if (pet.is_hungry == True):
                return True
        return False

    def eat(self):
        for pet in self.pets_list:
            pet.eat()

    def walk(self):
        for pet in self.pets_list:
            pet.walk()
            print(pet.name, "is walking!")

    # Prints content of Pet list
    def print_pets(self):
        print("I have ", len(self.pets_list), " cats")
        for pet in self.pets_list:
            print(pet.description())

        if (self.is_mammals() == True):
            print("And they're all mammals, of course.")
        else:
            print("And they're not all mammals.")

        self.eat()
        if (self.is_hunger() == True):
            print("My cats are hungry.")
        else:
            print("My cats are not hungry.")

# Runs Pets
animal_house = Pets()
animal_house.print_pets()
animal_house.walk()
