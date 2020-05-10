
class Data:

    def __init__(self, dia, mes, ano): #self é a referencia para encontrar o objeto quando criado
        print("Construindo objeto ... {}".format(self))
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))
