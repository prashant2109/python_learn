from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self._side = side

    def area(self):
        ara = self._side * self._side
        return ara

    def perimeter(self):
        per = self._side * 4
        return per 

#######################################################################################

class Payment:
    def print_split(self, amount):
        print(f'Purchase of {amount}')

    @abstractmethod
    def payment(self):
        pass

class CreditCardPayment(Payment):
    def payment(self, amount):
        print(f'Credit Card Payment of {amount}')

class MobileWalletPayment(Payment):
    def payment(self, amount):
        print(f'Mobile Wallet Payment of {amount}')



if __name__ == '__main__':
    sq = Square(5)
    print(sq.area())
    print(sq.perimeter())