class Dog(object):
	dogs = []

	def __init__(self, name):
		self.name = name
		self.dogs.append(self)

	@classmethod
	def num_dogs(cls):
		return len(cls.dogs)

	@staticmethod
	def bark(n):
		for _ in range(n):
			print(f"Bark!")


def main():
	d1 = Dog('Chow')
	d2 = Dog('Joe')


	print(Dog.num_dogs())

	d2.bark(5)


if __name__ == '__main__':
	main()
