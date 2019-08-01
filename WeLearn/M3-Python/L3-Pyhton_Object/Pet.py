pet = {
"name": "Doggo",
"animal": "dog",
"species": "labrador",
"age": 5
}

class Pet(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.animal = animal
        self.is_hungry = false
        self.mood = "happy"
        self.is_moving = walk


def eat(self):
    print("> %s is eating..." % self.name)
    if self.is_hungry: # This is equivalent to self.is_hungry
 self.is_hungry = false
else: # If the first test was false, and the pet wasn't is_hungry
print("> %s may have eaten too much." % self.name)
self.mood = "lethargic"

def move(self):
    print("> %s is moving..." % self.name)
    if self.is_moving:
        self.is_moving = false
else:
print("> %s walking way too much." % self.name)
self.mood = "Tired"

my_pet = Pet("Fido", 3, "dog")

print("My pet %s is %s years old" %(my_pet.name, my_pet.age))
my_pet.is_hungry = True # manually set to True
print("Is my pet hungry? %s" % my_pet.is_hungry)
my_pet.eat() # calls the eat method defined above
print("How about now? %s" % my_pet.is_hungry)
print("My pet is feeling %s" % my_pet.mood)

my_pet = Pet("boi", 15)
print("My pet %s is %s years old" %(my_pet.name, my_pet.age))

my_pet = Pet("rock", 1000000)
print("My pet %s is %s years old" %(my_pet.name, my_pet.age))
