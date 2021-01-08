class Animal:
    """Basic information about animals"""

    def __init__(self, name, color, animal_type, diet, cute):
        self.name = name
        self.color = color
        self.animal_type = animal_type
        self.diet = diet
        self.cute = cute

# help(Animal)

beluga = Animal('Beluga Whale', 'white', 'mammal', 'carnivore', True)
print(beluga.name)
print(beluga.color)
print(beluga.animal_type)
print(beluga.diet)
print(beluga.cute)

flying_squirrel = Animal('Flying Squirrel', 'brown', 'mammal', 'omnivore', True)
print(flying_squirrel.name)
print(flying_squirrel.color)
print(flying_squirrel.animal_type)
print(flying_squirrel.diet)
print(flying_squirrel.cute)

red_panda = Animal('Red Panda', 'red brown', 'mammal', 'omnivore', True)
print(red_panda.name)
print(red_panda.color)
print(red_panda.animal_type)
print(red_panda.diet)
print(red_panda.cute)