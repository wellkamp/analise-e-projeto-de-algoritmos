
def busca_sequencial(vetor, valor):
    i = 0
    while i < len(vetor):
        if vetor[i] == valor:
            return i
        i += 1

    return -1


def busca_sequencial_for(vetor, valor):
    for i in vetor:
        if vetor[i] == valor:
            return i

    return -1
