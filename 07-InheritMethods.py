class Person:
    name = ""
    age = ""

    def code(self):
        # agora, qualquer classe que herdar esta poderá programar
        print('Coding...')


class Student(Person):
    grade = 0.0

    def learn(self):
        print('Learning...')  # todo objeto Student podera aprender


class Teacher(Person):
    wage = 0.0

    def teach(self):
        print('Teaching...')  # todo objeto Teacher podera ensinar


# cria os objetos de acordo
ricardo = Teacher()
vitor = Student()

vitor.code()  # assim como atributos, metodos podem ser herdados
ricardo.code()
vitor.learn()  # mas, assim como atributos, também podem existir especificos
ricardo.teach()
# print(vitor.teach) e tentar acessar valores de outras subclasses nao funciona
