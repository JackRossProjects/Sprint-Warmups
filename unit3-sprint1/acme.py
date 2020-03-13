class Product():
    """ Class for products of ACME CORP """
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        """ Attributes of products """
        from random import randint
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        """ Determines stealability by using price:weight ratio """
        steal_ratio = (self.price / self.weight)
        if steal_ratio < 0.5:
            return "Not so stealable..."
        elif steal_ratio < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """ Determines if a product will exlode """
        boomboom = (self.flammability * self.weight)
        if boomboom < 10:
            return "...fizzle."
        elif boomboom < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """ Set up BoxingGloves subclass inheriting from Product class """
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...its a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"