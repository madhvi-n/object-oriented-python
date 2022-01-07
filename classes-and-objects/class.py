class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"Hi I am {self.name} and I am {self.age} years old."


class Cat(object):
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        return f"Hi I am {self.name} and I am {self.age} years old."



def main():
    tim = Dog('Tim', 8)
    print(tim.speak())

    mimi = Cat('Mimi', 7, 'white')
    print(mimi.speak())


if __name__ == "__main__":
    main()