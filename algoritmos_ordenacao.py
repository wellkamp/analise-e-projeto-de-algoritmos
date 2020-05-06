def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def selection_sort(A):
    for i in range(len(A)):

        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]


def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i-1
        while j >= 0 and chave < vetor[j]:
            vetor[j+1] = vetor[j]
            j -= 1
        vetor[j+1] = chave
