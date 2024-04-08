def merge_sort(arr, prof):
    if len(arr) > 1:
        meio = len(arr) // 2
        metade_esquerda = arr[:meio]
        metade_direita = arr[meio:]
        print(f"{'  ' * prof}Dividindo: {arr} -> {metade_esquerda} e {metade_direita}")
        merge_sort(metade_esquerda, prof + 1)
        merge_sort(metade_direita, prof + 1)
        i = j = k = 0
        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:
                arr[k] = metade_esquerda[i]
                i += 1
            else:
                arr[k] = metade_direita[j]
                j += 1
            k += 1
        while i < len(metade_esquerda):
            arr[k] = metade_esquerda[i]
            i += 1
            k += 1
        while j < len(metade_direita):
            arr[k] = metade_direita[j]
            j += 1
            k += 1
        print(f"{'  ' * prof}Merge: {metade_esquerda} e {metade_direita} -> {arr}")
    return arr

if __name__ == "__main__":
    arr = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Árvore de recursividade do Merge-Sort:")
    merge_sort(arr, 0)
