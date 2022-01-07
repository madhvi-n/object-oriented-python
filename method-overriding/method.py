class Point(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		self.coords = (self.x, self.y)

	def move(self, x, y):
		self.x += x
		self.y += y

	def __add__(self, p):
		return Point(self.x + p.x, self.y + p.y)

	def __sub__(self, p):
		return Point(self.x - p.x, self.y - p.y)

	def __mul__(self, p):
		return Point(self.x * p.x, self.y * p.y)

	def length(self):
		import math
		return math.sqrt(self.x ** 2, self.y ** 2)

	def __gt__(self, p):
		return self.length() > p.length()

	def __gte__(self, p):
		return self.length() >= p.length()

	def __lt__(self, p):
		return self.length() < p.length()

	def __lte__(self, p):
		return self.length() <= p.length()

	def __eq__(self, p):
		return self.x == p.x and self.y and p.y

	def __ne__(self, p):
		return not self.__eq__(p)

	def __str__(self):
		return f"({self.x}, {self.y})"

	def __repr__(self):
		return f"Point({self.x}, {self.y})"


def main():
	p1 = Point(2, 3)
	p2 = Point(4, 5)
	p3 = Point(1, 3)
	p4 = Point(0, 1)

	p5 = p1 + p2
	print(p5)

	p6 = p3 - p4
	print(p6)

	p7 = p2 - p4
	print(p7)

	print(dir(p1))


if __name__ == '__main__':
	main()