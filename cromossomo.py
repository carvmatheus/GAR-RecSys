import numpy as np
from main_ga import main

class CromossomoReal(object):
    

    def __init__(self, n):

        self.valores = np.zeros(n, dtype=np.float64)
        self.limites = np.zeros((n, 2), dtype=np.float64)

        # aqui temos que definir o range e quantas variaveis queremos otimizar

        self.setLimiteSuperior(0, 0.9)
        self.setLimiteInferior(0, 0.01)

        self.setLimiteSuperior(1, 0.9)
        self.setLimiteInferior(1, 0.01)


        

        for i in range(n):
            self.sorteiaPosicao(i)

    def sorteiaPosicao(self, i):
        self.valores[i] = self.limites[i][0] + np.random.random_sample() * (self.limites[i][1] - self.limites[i][0])

    def setLimiteInferior(self, i, val):
        if (i < len(self.valores)):
            self.limites[i][0] = val

            self.acertaValores(i)

    def getLimiteInferior(self, i):
        return (self.limites[i][0])

    def setLimiteSuperior(self, i, val):
        if (i < len(self.valores)):
            self.limites[i][1] = val

            self.acertaValores(i)

    def getLimiteSuperior(self, i):
        return (self.limites[i][1])

    def acertaValores(self, i):
        # Troca os limites, pois setamos o inferior para um valor maior
        # que o superior ou vice-versa
        if (self.limites[i][1] < self.limites[i][0]):
            temp = self.limites[i][1]
            self.limites[i][1] = self.limites[i][0]
            self.limites[i][0] = temp

            # Se o valor da psi��o passou a ficar fora dos novos limites setados, sorteia
        # um novo valor
        if ((self.valores[i] < self.limites[i][0]) or (self.valores[i] < self.limites[i][1])):
            self.sorteiaPosicao(i)

    def setPosicao(self, i, val):
        if (val < self.limites[i][0]):
            # essa funçao era lança um exceçao em java de limite inferio
            return "valor menor que o limite inferior"
        if (val > self.limites[i][1]):
            # essa funçao era lança um exceçao em java de limite inferio
            return "valor maior que o limite superior"
        self.valores[i] = val

    def getPosicao(self, i):
        return (self.valores[i])

    def crossoverSimples(self, outro):

        filho = CromossomoReal(len(self.valores))
        corte = round(np.random.random_sample() * len(self.valores))
        if (corte == len(self.valores)):
            corte -= 1
        for i in range(len(self.valores)):
            if (i < corte):
                minimo = self.getLimiteInferior(i)
                maximo = self.getLimiteSuperior(i)
                valor = self.getPosicao(i)
            else:
                minimo = outro.getLimiteInferior(i)
                maximo = outro.getLimiteSuperior(i)
                valor = outro.getPosicao(i)

            filho.setLimiteSuperior(i, maximo)
            filho.setLimiteInferior(i, minimo)

            try:
                filho.setPosicao(i, valor)
            except:
                print("nao conseguiu seta a posiçao no filho")
                # Nao precisamos fazer nada aqui, pois n�s j� acertamos os limites do
                # filho, e esta exce��o nunca ocorrer�.

        return filho

    def mutacao(self, chance):
        tamanho = len(self.valores)

        for i in range(tamanho):
            if (np.random.random_sample() <= chance):
                self.sorteiaPosicao(i)



    

    def calculaAvaliacao(self):
        # aqui temos que definir qual  função queremos maximizar 
        alpha = self.valores[0]
        beta = self.valores[1]
        
        self.avaliacao = main(alpha,beta)
        return self.avaliacao


    def getAvaliacao(self):
        return self.avaliacao