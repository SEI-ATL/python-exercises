class Juice:
    """ Storing fruits and their benefits """
    def __init__(self, fruit, benefits):
        self.fruit = fruit
        self.benefits = benefits

juice1 = Juice( "banana", "potasium")


print(juice1.benefits)