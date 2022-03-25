# cria uma classe para passar os atributos dos objetos
class Mouse:
    buttons = 2
    max_hz = 1000


# objetos (mouses) instanciados a partir da classe mouse
g_pro = Mouse()
hyperx = Mouse()

print(g_pro)  # tentar printar o objeto mostra o seu lugar na memória
print(hyperx.max_hz)
