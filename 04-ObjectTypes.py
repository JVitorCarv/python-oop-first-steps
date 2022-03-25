# Os atributos sao definidos de acordo com a classe
class Person:
    name = "joao"
    age = 23


class Vehicle:
    wheels = 4
    brand = "Chevrolet"


# camaro e um objeto do tipo veiculo
camaro = Vehicle()
# enquanto joao e um objeto do tipo pessoa, possuindo diferentes atributos
joao = Person()

print(camaro.wheels)  # tentar printar a qtd de rodas de um carro funciona
# print(camaro.age) mas tentar printar sua idade ocasionaria um erro

# print(joao.wheels) cada objeto tem seu tipo, e seus atributos são de acordo
print(joao.age)
