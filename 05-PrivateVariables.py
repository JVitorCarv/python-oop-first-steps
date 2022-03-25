class Car:
    __speed = 50  # Agora a variavel esta privada e so pode ser acessada dentro de metodos da classe

    # metodo getter para acessar o atributo speed
    def getSpeed(self):
        return self.__speed

    # metodo setter para alterar o atributo speed
    def setSpeed(self, speed):
        self.__speed = speed


camaro = Car()
camaro.setSpeed(100)  # muda o speed atraves do metodo setter
print(camaro.getSpeed())  # printa o speed atraves do metodo getter
