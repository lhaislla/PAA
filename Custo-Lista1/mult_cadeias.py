def matriz_cadeia_multiplicação(dimensões):
    n = len(dimensões) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                custo = m[i][k] + m[k+1][j] + dimensões[i] * dimensões[k+1] * dimensões[j+1]
                if custo < m[i][j]:
                    m[i][j] = custo
                    s[i][j] = k
    return m, s

def imprimir_parentização_ótima(s, i, j):
    if i == j:
        print("A{}".format(i + 1), end="")
    else:
        print("(", end="")
        imprimir_parentização_ótima(s, i, s[i][j])
        imprimir_parentização_ótima(s, s[i][j] + 1, j)
        print(")", end="")
        
if __name__ == "__main__":
    dimensões = [5, 10, 3, 12, 5, 50, 6]
    m, s = matriz_cadeia_multiplicação(dimensões)
    print("Parentização ótima:")
    imprimir_parentização_ótima(s, 0, len(dimensões) - 2)
    print()