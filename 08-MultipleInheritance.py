class Languages:
    python = True  # booleano para simbolizar que conhece


class Person:
    name = ""
    age = ""

    def code(self):
        print('Coding...')


class Student(Person, Languages):
    grade = 0.0

    def learn(self):
        print('Learning...')


class Teacher(Person, Languages):
    wage = 0.0

    def teach(self):
        print('Teaching...')


# cria os objetos de acordo
ricardo = Teacher()
vitor = Student()

# dessa forma, pode-se usar objetos de mais de uma classe diferente
print(vitor.python)
vitor.code()
print(ricardo.python)
ricardo.code()
