"""
Sources:
    - https://realpython.com/python3-object-oriented-programming/
"""

class Dog:
	# Class attribute
	species = 'Something'

	# Dunder methods (double underscrores) e.g. .__str__()
	def __init__(self, name, age):
		# Instance attributes
		self.name = name
		self.age = age

	# Instance method: functions defined within a class
	def description(self):
		return f"{self.name}"

	def speak(self, sound):
		return f"{sound}"

# super() tells Python to search parent class Dog() for .speak() method and calls it
class Dachshund(Dog):
	def speak(self, sound="default"):
		return super().speak(sound)

buddy = Dachshund("Buddy", 9)

print(buddy.name)
print(buddy.age)
print(buddy.speak("pass here"))