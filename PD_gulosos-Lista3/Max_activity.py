import heapq 
def max_atividade_selecionada(s, f, v, n):
    """
    Seleciona o conjunto máximo de atividades não sobrepostas com o máximo de valor.

    Args:
        s (list): Tempos de início das atividades.
        f (list): Tempos de término das atividades.
        v (list): Valores das atividades.
        n (int): Número de atividades.

    Returns:
        int: Valor máximo das atividades selecionadas.
    """
    atividades = [(fim, inicio, valor) for fim, inicio, valor in zip(f, s, v)]
    heapq.heapify(atividades)
    selecao = []
    valor_total = 0
    for _ in range(n):
        fim, inicio, valor = heapq.heappop(atividades)
        if not selecao or inicio >= selecao[-1][1]:
            selecao.append((fim, inicio, valor))
            valor_total += valor
            print(valor_total)
    return valor_total

s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
v = [50, 20, 70, 40, 30, 10]
n = len(s)

print(max_atividade_selecionada(s, f, v, n))