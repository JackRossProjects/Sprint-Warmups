from random import randint, sample, uniform
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(number_of_products=30):
    """
    Creates 30 random products
    """
    generated_products = []

    for x in range(number_of_products):
        adjective = sample(ADJECTIVES, 1)[0]
        noun = sample(NOUNS, 1)[0]
        name = adjective + ' ' + noun
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        prod = Product(name, price, weight, flammability)
        generated_products.append(prod)
    return generated_products

def inventory_report(products):
    """
    Prints out the inventory report
    """
    names_list = []
    weights_list = []
    prices_list = []
    flammability_list = []

    for product in products:
        names_list.append(product.name)
        weights_list.append(product.weight)
        prices_list.append(product.price)
        flammability_list.append(product.flammability)

    unique_products = (len(set(names_list)))
    mean_weight = (sum(weights_list) / len(weights_list))
    mean_price = (sum(prices_list) / len(prices_list))
    mean_flammability = (sum(flammability_list) / len(flammability_list))

    print(f"ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print(f"Unique Product Names: {unique_products}")
    print(f"Average Price: {mean_price}")
    print(f"Average Weight: {mean_weight}")
    print(f"Average Flammability: {mean_flammability}")

if __name__ == '__main__':
    inventory_report(generate_products())