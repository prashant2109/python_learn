import datetime
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    @classmethod
    def fromBirthYear(cls, name, b_year):
        age = datetime.datetime.today().year - b_year
        return cls(name, age)

    @staticmethod
    def age_condition(age):
        return age > 18

if __name__ == '__main__':
    d_Obj = Person.fromBirthYear('Dan', 1991)
    print(d_Obj.age) 
    # p_Obj = Person('Mayank', 21)
    # print(p_Obj.age_condition(p_Obj.age))



