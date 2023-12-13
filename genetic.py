
#from CromossomoReal import CromossomoReal
import numpy as np
from cromossomo import CromossomoReal

class GA:
    qtdVar = 2
    Ks=0

    def __init__(self, num_geracoes, tam_populacao, prob_mut):
        self.chance_mutacao = prob_mut;
        self.numero_geracoes = num_geracoes;
        self.tamanho_populacao = tam_populacao;        
        self.dic={}

    # @numba.jit
    def inicializaPopulacao(self):
        self.populacao = [CromossomoReal(self.qtdVar) for i in range(self.tamanho_populacao)]
        
    def avaliaTodos(self):
        # essa func cria 3 atributos para a classe, avaliacao, melhor e somaAvaliacoes
        # cria uma lista das avaliacoes
        self.avaliacao = list(map(lambda x: x.calculaAvaliacao(), self.populacao))
        # testar depois self.avaliacao=[i.calculaAvaliacao() for i in range(self.populacao)]
        # pega o endereco do individo de valor maior
        self.melhor = self.avaliacao.index(max(self.avaliacao))
        self.somaAvaliacoes = sum(self.avaliacao)

    def roleta(self):
        limite = np.random.random_sample() * self.somaAvaliacoes
        i = 0
        aux = 0
        while ((i < self.tamanho_populacao) and (aux < limite)):
            aux += self.avaliacao[i]
            i += 1
        # Como somamos antes de testar, então tiramos 1 de i pois
        # o anterior ao valor final consiste no elemento escolhido
        i -= 1

        return (i)


    def geracao(self):
        self.nova_populacao = []
        self.nova_populacao.append(self.populacao[self.melhor])  # eletismo
        # ini = time.time()
        #print("Calculando nova geracao...\n")

        for i in range(self.tamanho_populacao - 1):
            pai1 = self.populacao[self.roleta()]
            pai2 = self.populacao[self.roleta()]

            filho = pai1.crossoverSimples(pai2)
            filho.mutacao(self.chance_mutacao)
            self.nova_populacao.append(filho)
        # fim = time.time()
        # print ("tempo de geracao: ", fim-ini)

    def moduloPopulacao(self):
        # del self.populacao
        self.populacao = self.nova_populacao
        del self.nova_populacao


    def executa(self):

        self.inicializaPopulacao()

        for i in range(self.numero_geracoes):
            self.avaliaTodos()
            #self.imprime()
            # print(self.populacao[0].valores[0])
            self.geracao()

            self.moduloPopulacao()
        self.imprime()

    def imprime(self):
        '''print('x=', self.populacao[self.melhor].valores[0],
              '\ny=', self.populacao[self.melhor].valores[1],
              '\nz=', self.populacao[self.melhor].valores[2],
              '\nt=', self.populacao[self.melhor].valores[3],
              '\nAvaliacao=', self.avaliacao[self.melhor])'''
        print('alpha= ',self.populacao[self.melhor].valores[0])
        print('beta= ',self.populacao[self.melhor].valores[1], '\nAvaliacao=', self.avaliacao[self.melhor])
        print()

