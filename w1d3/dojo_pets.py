class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
    
    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.make_noise()

class Pet:
    def __init__(self, name , type , tricks, noise ):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 0
        self.health = 0
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self

    def eat(self): 
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def make_noise(self):
        print(self.noise)
        return self


pet_1 = Pet("Peanut", "weiner dog", "sit, stay, lay-down, up", "woof")

ninja_1 = Ninja("Larry", "Walls", "Becker Bites", "small breed", pet_1)


ninja_1.walk()
print(pet_1.health)

ninja_1.walk()
print(pet_1.health)

ninja_1.bathe()
