import heapq
def heap_max(conjunto):
    """
    Recebe um conjunto e o ordena em ordem decrescente usando heap de máximo.
    Args:
        A (list): Conjunto de inteiros.
    Returns:
        list: Conjunto ordenado em ordem decrescente.
    """
    heapq._heapify_max(conjunto)
    heap = []
    while conjunto:
        heap.append(heapq._heappop_max(conjunto))
    return heap

def max_pag(A, B):
    """
    Calcula o pagamento máximo dado os conjuntos A e B.
    Args:
        A (list): Conjunto de inteiros.
        B (list): Conjunto de inteiros.   
    Returns:
        int: Pagamento máximo.
    """
    pagamento = 1
    for a, b in zip(A, B):
        pagamento *= a ** b
    return pagamento

A = [4, 3, 2]
B = [3, 2, 1]
conjunto_ordenado_A = heap_max(A)
conjunto_ordenado_B = heap_max(B)
print(conjunto_ordenado_A)
print(conjunto_ordenado_B)
print(max_pag(conjunto_ordenado_A, conjunto_ordenado_B))
