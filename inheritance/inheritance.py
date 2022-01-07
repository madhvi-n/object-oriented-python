class Vehicle(object):
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fill_tank(self):
        self.gas = 100

    def empty_gas(self):
        self.gas = 0

    def gas_left(self):
        return self.gas


class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        return f"Beep!"


class Truck(Car):
    def __init__(self, price, gas, color, speed, tires):
        super().__init__(price, gas, color, speed)
        self.tires = tires

    def get_tires(self):
        return self.tires

    def beep(self):
        return f"Honk!!"


def main():
    truck = Truck(1000, 23, 'blue', 78, 4)
    print(truck)
    print(truck.beep())


if __name__ == "__main__":
    main()