# EXERCISE
# Create different subclasses of an Animal class that return different values 
# for a speak() method.

class Animal:
    def speak(self):
        return 'Raaa!'

class Cat:
    def speak(self):
        return 'Meow!'

class Dog:
    def speak(self):
        return 'Woof!'

class GuineaPig:
    def speak(self):
        return 'Wheek!'

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    tigger = Cat()
    fido = Dog()
    dobbins = GuineaPig()

    print(f"The cat says \"{tigger.speak()}\"")
    print(f"The dog says \"{fido.speak()}\"")
    print(f"The guinea pig says \"{dobbins.speak()}\"")