# EXERCISE
# Create a Taxi class that expands a Vehicle class. The taxi class adds 
# a 10% maintenance fee on top of a Vehicle's standard base fare.

class Vehicle:
    def __init__(self, baseFare: float):
        self.baseFare = baseFare
        self.maintenanceFee = 0

    def totalFare(self) -> float:
        return self.baseFare + self.maintenanceFee

class Taxi(Vehicle):
    def __init__(self, baseFare: float):
        super().__init__(baseFare)
        self.maintenanceFee = baseFare * 0.10

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    bus = Vehicle(50)
    print(f"Bus total fare: {bus.totalFare()}")
    cab = Taxi(50)
    print(f"Taxi total fare: {cab.totalFare()}")