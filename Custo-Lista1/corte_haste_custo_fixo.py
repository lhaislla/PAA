def Extended_Bottom_Up_Cut_Rod(p, n, c):
    R = [0] * (n + 1) #R e S armazenam receitas máximas e cortes ótimos
    S = [0] * (n + 1)
    for j in range(1, n + 1): 
        q = float('-inf')
        for i in range(1, j + 1):
            if q < p[i] + R[j - i] - c:
                q = p[i] + R[j - i] - c
                S[j] = i
        R[j] = q
    return R, S

def Print_Cut_Rod_Solution(S, n):
    solucao = []
    while n > 0:
        solucao.append(S[n])
        n = n-S[n]
    return solucao

if __name__ == "__main__":
    precos = [0, 1, 5, 8, 9, 10, 17, 17, 20]
    comprimento = 3
    custo_corte = 2
    receitas, cortes_optimos = Extended_Bottom_Up_Cut_Rod(precos, comprimento, custo_corte)
    solucao = Print_Cut_Rod_Solution(cortes_optimos, comprimento)
    print("Receitas máximas:", receitas)
    print("Cortes ótimos:", cortes_optimos)
    print("Solução ótima (comprimentos de corte):", solucao)
