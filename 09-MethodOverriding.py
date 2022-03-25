class Dog:
    def bark(self):
        print('woof woof')


class Pitbull(Dog):
    name = "Pitbull"

    def bark(self):  # o pitbull tambem tem um bark
        print('WOOF WOOF')


class Poodle(Dog):
    name = "Poodle"


dog1 = Poodle()
dog2 = Pitbull()

dog1.bark()  # nesse caso, so ha 1 metodo bark
dog2.bark()  # nesse, o metodo da subclasse e priorizado
