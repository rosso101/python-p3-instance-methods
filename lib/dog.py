class Dog:
  def bark(self):
    print("Woof!")

fido = Dog()
fido.bark()
# Woof!

fido.sit()
# AttributeError: 'Dog' object has no attribute 'sit'