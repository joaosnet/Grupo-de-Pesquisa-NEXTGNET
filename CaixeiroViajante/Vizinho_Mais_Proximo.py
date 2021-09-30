import numpy as np


class VizinhoMaisProximo:

    # Instancia a classe
    def __init__(self, cInicial, cFinal):
        self.cidadeInicial = cInicial
        self.cidadeFinal = cFinal
        self.vetorCaminho = []
        self.linha = []
        self.unidadeTotal = 0
        self.vetorCaminho.append(cInicial)

    # Ler a arquivo da matriz
    def lerMatriz(self, nomeMatriz):
        global nCidades
        global matriz

        # Ler o arquivo das rotas
        with open(nomeMatriz) as matrizRotas:
            r = matrizRotas.readline()  # Lê a primeira linha(Número de cidades)
            nCidades = int(r)           # Transforma em inteiro

            # Inicializa a matriz através da biblioteca numpy
            matriz = np.arange(nCidades * nCidades).reshape(nCidades, nCidades)  # verificar
            r = matrizRotas.readline().split()

            # Escreve as rotas na matriz linha por linha
            for l in range(0, nCidades):
                for c in range(0, nCidades):
                    matriz[l][c] = r[c]
                r = matrizRotas.readline().split()

            print(matriz)
            print('='*40)

    # Cria a rota passando pelas ciades até a cidade final
    def criarRota(self):
        while self.vetorCaminho[len(self.vetorCaminho)-1] != self.cidadeFinal:
            l1 = self.vetorCaminho[len(self.vetorCaminho)-1]-1
            l2 = self.vetorCaminho[len(self.vetorCaminho)-1]
            self.menorCaminho(l1, l2)
            #self.proximaCidade(self.vetorCaminho[len(self.vetorCaminho)-1])
        # self.unidadeTotal += self.linha[self.cidadeInicial - 1]
        # self.vetorCaminho.append(self.cidadeInicial)
        #print('='*40)

    # chama a proxima cidade
    #def proximaCidade(self, linha):
        #self.menorCaminho(linha-1, linha)

    # Verifica qual o menor caminho a ser seguido
    def menorCaminho(self, l1, l2):

        self.linha = matriz[l1:l2].flatten()  # Rota da cidade em relação as outras
        num = l2
        menor = 999
        aux = 0
        print('Linha {}: {}'.format(num,self.linha))
        for l in range(0, nCidades):
            contem = self.verificaCaminho(l+1)
            if self.linha[l] < menor and self.linha[l] != 0 and not contem:
                menor = self.linha[l]
                aux = l+1

        self.vetorCaminho.append(aux)
        self.unidadeTotal += menor
        print('Menor caminho: ', menor)
        print('Cidade escolhida: ', self.vetorCaminho[len(self.vetorCaminho)-1])
        print('Rota: ', self.vetorCaminho)
        print('='*40)

    # Verifica se a cidade já foi visitada
    def verificaCaminho(self, cidade):
        contem = False
        for c in range(0, len(self.vetorCaminho)):
            if cidade == self.vetorCaminho[c]:
                contem = True
        return contem

    # Imprime o resultado
    def imprime(self):
        print('Cidade Inicial: ', self.cidadeInicial)
        print('Rota completa: ', self.vetorCaminho)
        print('Unidade Total = ', self.unidadeTotal)
