import sys
def matrix_chain_order(dimensoes):
    n = len(dimensoes) - 1  # número de matrizes
    memoizacao = [[0] * (n+1) for _ in range(n+1)]  # tabela de memoização
    divisao_otima = [[0] * (n+1) for _ in range(n+1)]  # Registro da posição ótima de divisão

    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            memoizacao[i][j] = sys.maxsize  # Maior valor possível
            for k in range(i, j):
                q = memoizacao[i][k] + memoizacao[k+1][j] + dimensoes[i-1] * dimensoes[k] * dimensoes[j]
                if q < memoizacao[i][j]:
                    memoizacao[i][j] = q
                    divisao_otima[i][j] = k

    return memoizacao, divisao_otima

def matrix_chain_multiply(dimensoes, divisao_otima, i, j):
    if i == j:
        return dimensoes[i-1][0], dimensoes[i-1][1]
    inicio_esquerda, fim_esquerda =  matrix_chain_multiply(dimensoes, divisao_otima, i, divisao_otima[i][j])
    inicio_direita, fim_direita =  matrix_chain_multiply(dimensoes, divisao_otima, divisao_otima[i][j] + 1, j)
    if fim_esquerda != inicio_direita:
       return ("Incompatibilidade de matrizes")
    matriz_resultante = [[0] * (fim_direita - inicio_esquerda + 1) for _ in range(fim_esquerda - inicio_esquerda + 1)]
    for linha in range(fim_esquerda - inicio_esquerda + 1):
        for coluna in range(fim_direita - inicio_esquerda + 1):
            for k in range(fim_esquerda - inicio_esquerda + 1):
                matriz_resultante[linha][coluna] += dimensoes[inicio_esquerda-1 + linha][k] * dimensoes[k][fim_esquerda + coluna]
    return inicio_esquerda, fim_direita, matriz_resultante

def print_optimal_parens(divisao_otima, i, j):
    if i == j:
        print("A{}".format(i), end='')
    else:
        print("(", end='')
        print_optimal_parens(divisao_otima, i, divisao_otima[i][j])
        print_optimal_parens(divisao_otima, divisao_otima[i][j] + 1, j)
        print(")", end='')
if __name__ == "__main__":
    # Entrada: Lista de tuplas das dimensões das matrizes. Cada tupla representa uma matriz com dimensões (linhas, colunas).
    dimensoes_matrizes = [(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]
    tabela_memoizacao, divisao_otima =  matrix_chain_order([dim[0] for dim in dimensoes_matrizes])
    print("Ordem ótima da multiplicação:")
    print_optimal_parens(divisao_otima, 1, len(dimensoes_matrizes)-1)
    print()
    print("\nTabela de memoização:")
    for linha in tabela_memoizacao:
        print(linha)
