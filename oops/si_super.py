class Mammal:
    def __init__(self, mammal_name):
        print (f'This is a {mammal_name}')
    
class Dog(Mammal):
    def __init__(self):
        print('Is a domestic animal')
        super().__init__('Dog')

######################################################################################################
class Computer:
    def __init__(self, computer, ram, storage):
        self.computer = computer
        self.ram      = ram
        self.storage  = storage

class Mobile(Computer):
    def __init__(self, computer, ram, storage, model):
        super(Mobile, self).__init__(computer, ram, storage)
        self.model = model


if __name__ == '__main__':
    c_Obj = Mobile('Apple', 2, 64, 'iphone X')
    print(c_Obj.model)
