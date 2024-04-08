def bottom_up_cut_rod(p, n, c):
    r = [0] * (n + 1)
    custofinal = 0
    for j in range(1, n + 1):
        q = float("-inf")
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
            custofinal += c
        r[j] = q
    return (r[n] + custofinal)

if __name__ == "__main__":
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  #Preços de haste
    n = 4  # Tamanho da haste a ser cortada
    c = 1  # Custo
    resultado = bottom_up_cut_rod(p, n, c)
    print("O valor máximo que pode ser obtido cortando uma haste de tamanho", n, "é:", resultado)
