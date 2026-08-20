# EXERCISE
# Create a shopping cart class that can hold various products and quantities. 
# Create dunder methods so that using the len function on the class returns 
# the number of items in the cart, individual entries in the cart can be accessed 
# directly, and the cart can be looped over.

# A very basic Product class to put into our Shopping Cart
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.__contents = {}

    def add(self, prod: Product, quantity: int = 1):
        if prod.name in self.__contents:
            self.__contents[prod.name]['quantity'] += quantity
        else:
            self.__contents[prod.name] = {'price': prod.price, 'quantity': quantity}

    # __len__ magic (or "dunder" for "double underscore") method to give Python instructions
    # on what to do if we use the len() function on the object.
    def __len__(self):
        qty = 0
        # Loop through the contents and add up the quantities of each Product
        for info in self.__contents.values():
            qty += info['quantity']
        return qty

    # __getitem__ magic method to tell Python how to handle passing an index to the cart.
    def __getitem__(self, index):
        return self.__contents[index]

    # __iter__ magic method to tell Python how to loop over the cart. In this case,
    # we will just loop over the key-value pairs of the internal dictionary.
    def __iter__(self):
        return iter(self.__contents.items())

    def totalPrice(self):
        total = 0.0
        for info in self.__contents.values():
            total += info['price'] * info['quantity']
        return total

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    ups = Product('UPS Battery Backup', 349.99)
    robot = Product('STEM Robot Building Kit', 53.99)
    toy = Product('Transformers Studio Series Movie Perceptor', 42.99)

    cart = ShoppingCart()
    cart.add(ups)
    cart.add(robot, 2)
    cart.add(toy, 4)

    print(f"There are {len(cart)} items in the shopping cart.")
    print(f"Total cost: ${cart.totalPrice():.2f}")

    print(f"Number of Perceptors and total cost: {cart[toy.name]['quantity']} for ${cart[toy.name]['price']:.2f} each.")

    print()
    print('CART')
    print('=' * 4)
    for name, info in cart:
        print(f"{name}: {info['quantity']} for ${info['price'] * info['quantity']:.2f}")