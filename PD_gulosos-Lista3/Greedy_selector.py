from heapq_max import *

def greedy_atividade_selector(s, f, v):
    n = len(s)
    atividades = [(s[i], f[i], v[i]) for i in range(n)]
    atividades.sort(key=lambda x: x[1], reverse=True)  # Atividades ordenadas por tempo de término (decrescente).

    heapify_max(atividades)  # Transforma a lista de atividades em um heap de máximo

    selected_atividades = []
    tempo_termino = 0

    for atividade in atividades:
        tempo_inicio, finish_time, value = atividade
        if tempo_inicio >= tempo_termino:
            selected_atividades.append(atividade)
            tempo_termino = finish_time

    return selected_atividades

# Exemplo de utilização
s = [1, 2, 4, 6, 8]
f = [3, 5, 7, 9, 10]
v = [5, 6, 4, 7, 2]

selected = greedy_atividade_selector(s, f, v)
print("Atividades selecionadas:")
for atividade in selected:
    print("Inicio:", atividade[0], "Término:", atividade[1], "Valor:", atividade[2])
