class Dog:
    # metodo de latir de um cachorro
    def bark(self):  # toda vez que uma funcao e criada dentro de uma classe ela deve receber self
        print('Woof woof!')

    # metodo de comer de um cachorro
    def eat(self):
        print('Eating')


# todo cachorro tem o metodo latir
bulldog = Dog()
poodle = Dog()
retriever = Dog()

# print para checar
bulldog.bark()
poodle.bark()
retriever.eat()
