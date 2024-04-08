def memoized_cut_rod(p, n):
    r = [-float('inf')] * (n + 1)
    s = [-1] * (n + 1)
    return memoized_cut_rod_aux(p, n, r, s)

def memoized_cut_rod_aux(p, n, r, s):
    if r[n] >= 0:
        return r[n], s
    if n == 0:
        return 0, s
    q = -float('inf')
    for i in range(1, n + 1):
        temp, _ = memoized_cut_rod_aux(p, n - i, r, s)
        if q < p[i] + temp:
            q = p[i] + temp
            s[n] = i
    r[n] = q
    return q, s

if __name__ == "__main__":
    precos = [0, 1, 5, 8, 9, 10, 17, 17, 20]
    comprimento = 8

    valor_optimo, cortes_optimos = memoized_cut_rod(precos, comprimento)
    print("Valor ótimo:", valor_optimo)
    print("Cortes ótimos:", cortes_optimos)
