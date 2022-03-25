from abc import ABC, abstractmethod  # importa o abstract method do modulo abc


class Animal(ABC):  # recebe o ABC para usar o abstractmethod e criar um metodo abstrato
    @abstractmethod
    def sound(self):
        pass
    # dessa forma, qualquer subclasse precisará de um método sound para instanciar um objeto


class Cat(Animal):
    # se você tentar instanciar um objeto Cat sem a classe ter um metodo sound, um erro ocorrera
    def sound(self):
        print('Meow')


class Dog(Animal):
    # independentemente de implementacao, um metodo sound há de existir
    def sound(self):
        print('Woof')


garfield = Cat()
courage = Dog()

garfield.sound()
courage.sound()
