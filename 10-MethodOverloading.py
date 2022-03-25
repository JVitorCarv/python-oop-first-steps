class Person:
    def goodMorning(self, name=None):  # caso nenhum name venha, seu valor será None
        if name is None:  # dessa forma, irá printar sem name
            print('Good morning!')
        else:  # caso name tenha sido sobrescrito
            print(f'Good morning {name}!')


dwight = Person()
jim = Person()

jim.goodMorning('Jim')  # passamos o nome como parâmetro
dwight.goodMorning()  # nao passamos o nome como parametro
