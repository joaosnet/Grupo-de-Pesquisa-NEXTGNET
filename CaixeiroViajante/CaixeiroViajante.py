import time
from Vizinho_Mais_Proximo import VizinhoMaisProximo


# INICIO

cidadeInicial = 1
cidadeFinal = 5
inicio = time.time()
v = VizinhoMaisProximo(cidadeInicial, cidadeFinal)
v.lerMatriz('10_05_31')
v.criarRota()
v.imprime()
fim = time.time()
diferenca = fim - inicio
print('Tempo de execução', diferenca)

