from random import seed
from random import randint

class Soup:
    """ The Soup class sets up an object for hot and cold soups with their ingredients.  Call .review() to get the Soup Class's opinion of the soup """

    def __init__ (self, name, temperature, ingredients):
        self.name = name
        self.temperature = temperature #hot or cold
        self.ingredients = ingredients #array
    
    def get_shopping_list(self):
        """ Return Ingredients in a nicely formatted shopping list """
        list = "\n- ".join(self.ingredients)
        print("- " + list)
        return "- " + list
    
    def get_review(self):
        """ Get Soup Classes's opinion on your soup """
        opinions = ["ok...", "no.", "Gross", "But why though"]
        if self.temperature.lower() == "cold": 
            seed()
            ind = randint(0, len(opinions)-1)
            return opinions[ind]


borscht = Soup("Borscht", "Cold", ["Beets", "Dill", "Sour Cream", "Potatoes (optional)"])


print(borscht.name)

borscht.get_shopping_list()

print(borscht.get_review())

help(Soup)