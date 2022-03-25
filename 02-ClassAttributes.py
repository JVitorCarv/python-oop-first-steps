# cada classe tem atributos que serão instanciados para os objetos, mas os valores podem mudar
class Car:
    color = ""
    door = 0


# Passa os valores para os atributos color e door de acordo com o modelo do carro
fusca = Car()
fusca.door = 2
fusca.color = "Yellow"

civic = Car()
civic.door = 4
civic.color = "Black"

# print de checagem
print(fusca.door)
print(fusca.color)
print(civic.door)
print(civic.color)
