def fibonacci(n):
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

if __name__ == "__main__":
    n = 100
    print("O", n, "-ésimo número de Fibonacci é:", fibonacci(n))
