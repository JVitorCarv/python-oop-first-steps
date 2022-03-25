# cria a superclasse Person, que passará seus atributos name e age para quem se extender dela
class Person:
    name = ""
    age = ""

# cria a classe Student, que recebe os atributos de Person, tornando-os disponiveis para seus objetos


class Student(Person):
    grade = 0.0  # atributo que apenas estara em Student

# assim como Student, recebe os atributos de Person e os torna disponiveis para seus objetos


class Teacher(Person):
    wage = 0.0  # atributo que apenas estara em Teacher


# cria os objetos de acordo
ricardo = Teacher()
ricardo.name = "Ricardo"
ricardo.wage = 1000000

vitor = Student()
vitor.name = "Vitor"
vitor.grade = 10

print(ricardo.name)  # agora posso acessar atributos de Person
print(ricardo.wage)  # bem como atributos de Teacher
print(vitor.name)
print(vitor.grade)
# print(vitor.wage) mas tentar acessar valores de outras subclasses nao funciona
# print(ricardo.grade)
