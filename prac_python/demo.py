class Dog:
	def __init__(self, breed):
		self.breed = breed

	@classmethod
	def create_dog(cls,breed):
		return cls(breed)

pug = Dog.create_dog("Pug")
print(pug.breed)

