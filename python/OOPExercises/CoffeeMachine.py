# EXERCISE
# Create a Coffee Machine class. The class should manage quantities of coffee, water, and milk.
# There should also be a "make latte" method that refuses if there are insufficent ingredients.

class CoffeeMachine:
    def __init__(self, water: int, coffee: int, milk: int):
        self.water = water
        self.coffee = coffee
        self.milk = milk

    # This method makes use of keyword arguments. The arguments *must* invoked by name, and they 
    # are passed into the method body as a dictionary.
    def add(self, **ingredients: int) -> bool:
        for ingredient, quantity in ingredients.items():
            if ingredient == 'water':
                self.water += quantity
            elif ingredient == 'coffee':
                self.coffee += quantity
            elif ingredient == 'milk':
                self.milk += quantity
        return True

    # Check to see if we have the ingredients to make a latte. If so, deduct the ingredient 
    # quantities and announce that we've made a latte.
    def makeLatte(self) -> bool:
        # Requirements: 200 water, 20 coffee, 150 milk
        if self.water >= 200 and self.coffee >= 20 and self.milk >= 150:
            self.water -= 200
            self.coffee -= 20
            self.milk -= 150
            print('One latte.')
            return True
        else:
            # Log that we've run out of ingredients.
            print('Machine needs to be restocked.')
            return False

    # Check to see our ingredient quantities
    def checkStock(self) -> bool:
        print(f"Stock: {self.water} water, {self.coffee} coffee, {self.milk} milk")

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    cm = CoffeeMachine(500, 100, 500)
    cm.makeLatte()
    cm.makeLatte()
    cm.makeLatte()
    cm.add(water=300)
    cm.makeLatte()
    cm.add(milk=300)
    cm.makeLatte()