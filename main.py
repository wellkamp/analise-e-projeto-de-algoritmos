import time
import random

from algoritmos_ordenacao import mergeSort
from algoritmos_ordenacao import selection_sort
from algoritmos_ordenacao import insertion_sort
from busca_sequencial import busca_sequencial, busca_sequencial_for


def main():
    # Array de entradas utilizado nos Algoritmos de Ordenação
    arr = [250, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000, 200000]
    n = len(arr)
    # Array de entradas utilizado no Algoritmo de busca
    # arr = [1000000, 2500000, 5000000, 7500000, 9000000, 10000000,
    #              25000000, 50000000, 75000000, 80000000]
    n2 = len(arr)

    print("Busca Sequencial com FOR")
    for i in range(n2):
        vetor = list(range(0, arr[i] + 1))
        # random.shuffle(vetor)
        antes = time.time_ns() / (10 ** 9)
        posicao = busca_sequencial_for(vetor, arr[i])
        depois = time.time_ns() / (10 ** 9)
        total = (depois - antes)
        if posicao >= 0:
            print("O elemento: ", arr[i], " foi encontrado na posicao: %d" %
                  posicao + " com tempo de: %0.5f s" % total)
        else:
            print("Elemento não encontrado")

    print("Busca Sequencial com WHILE")

    for j in range(n2):
        vetor = list(range(0, arr[j] + 1))
        # random.shuffle(vetor)
        antes = time.time_ns() / (10 ** 9)
        posicao = busca_sequencial(vetor, arr[j])
        depois = time.time_ns() / (10 ** 9)
        total = (depois - antes)
        if posicao >= 0:
            print("O elemento: ", arr[j], " foi encontrado na posicao: %d" %
                  posicao + " com tempo de: %0.5f s" % total)
        else:
            print("Elemento não encontrado")

    for k in range(n):
        # Faz um vetor de 0 até o tamanho da entrada
        print('Tamanho da entrada: ', arr[k])
        vetor = list(range(0, arr[k]))
        # print(vetor)
        # Embaralha o vetor
        random.shuffle(vetor)

        # Copiando os vetores para deixar todos iguais para os algoritmos
        vm = vetor.copy()
        vi = vetor.copy()
        vs = vetor.copy()

        # Chamando o algoritmo Merge
        antes = time.time_ns() / (10 ** 9)
        mergeSort(vm)
        depois = time.time_ns() / (10 ** 9)
        total = (depois - antes)
        print("Merge Sort: %0.5f s" % total)

        # Chamando o algoritmo Insertion
        antes = time.time_ns() / (10 ** 9)
        insertion_sort(vi)
        depois = time.time_ns() / (10 ** 9)
        total = (depois - antes)
        print("Insertion Sort: %0.5f s" % total)

        # Chamando o algoritmo Selection
        antes = time.time_ns() / (10 ** 9)
        selection_sort(vs)
        depois = time.time_ns() / (10 ** 9)
        total = (depois - antes)
        print("Selection Sort: %0.5f s" % total)


if __name__ == '__main__':
    main()
