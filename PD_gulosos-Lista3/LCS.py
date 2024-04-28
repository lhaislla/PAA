def Reconstroi_LCS(c, X, Y, i, j):
    if i == 0 or j == 0:
        return
    if X[i - 1] == Y[j - 1]:
        Reconstroi_LCS(c, X, Y, i - 1, j - 1)
        print(X[i - 1])
    elif c[i - 1][j] >= c[i][j - 1]:
        Reconstroi_LCS(c, X, Y, i - 1, j)
    else:
        Reconstroi_LCS(c, X, Y, i, j - 1)

# Exemplo de uso:
X = "ABCBDAB"
Y = "BDCAB"
c = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 2, 2],
    [0, 1, 1, 2, 2, 2],
    [0, 1, 2, 2, 2, 3],
    [0, 1, 2, 2, 3, 3],
    [0, 1, 2, 3, 3, 4]
]

Reconstroi_LCS(c, X, Y, len(X), len(Y))
