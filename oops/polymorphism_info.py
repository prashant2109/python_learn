# Method Overriding


# Same method in 2 classes but gives the different output, this is known as polymorphism.
class Bank:
    def rateOfInterest(self):
        return 0

class ICICI(Bank):
    def rateOfInterest(self):
        return 10.5

if __name__ == '__main__':
    b_Obj = Bank()
    print(b_Obj.rateOfInterest())

##############################################################################################33

# Polymorphism with class
class Cat:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f'My name is {self.name}. I belong to cat family.')

    def make_sound(self):
        print('meow')

class Dog:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f'My name is {self.name}. I belong to Dog family.')

    def make_sound(self):
        print('Bark')

cat = Cat('kitty')
dog = Dog('tommy')

# Here we are calling methods of 2 different class types with common variable 'animal' 

for animal in (cat, dog):
    print(animal.info())
    print(animal.make_sound())

#############################################################################################################
class India():
     def capital(self):
       print("New Delhi")
 
     def language(self):
       print("Hindi and English")
 
class USA():
     def capital(self):
       print("Washington, D.C.")
 
     def language(self):
       print("English")
 
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()

########################################################################################################
class Bird:
     def intro(self):
       print("There are different types of birds")
 
     def flight(self):
       print("Most of the birds can fly but some cannot")
 
class parrot(Bird):
     def flight(self):
       print("Parrots can fly")
 
class penguin(Bird):
     def flight(self):
       print("Penguins do not fly")
 
obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()
 
obj_bird.intro()
obj_bird.flight()
 
obj_parr.intro()
obj_parr.flight()
 
obj_peng.intro()
obj_peng.flight()
