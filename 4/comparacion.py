import time
import matplotlib.pyplot as plt
from cyk import cyk_parse
from predictivo import ParserLL

def generate_input(n):
    # Alterna operadores: + - * /
    ops = ["+", "-", "*", "/"]
    tokens = []

    for i in range(n):
        tokens.append("num")
        if i < n - 1:
            tokens.append(ops[i % len(ops)])

    return tokens

def measure():
    sizes = [3, 5, 7, 9, 11]
    cyk_times = []
    ll_times = []

    for size in sizes:
        tokens = generate_input(size)

        # CYK
        start = time.time()
        cyk_parse(tokens)
        cyk_time = time.time() - start

        # LL
        start = time.time()
        parser = ParserLL(tokens)
        parser.parse()
        ll_time = time.time() - start

        cyk_times.append(cyk_time)
        ll_times.append(ll_time)

        print(f"Tamaño {len(tokens)} → CYK: {cyk_time:.6f}s | LL: {ll_time:.6f}s")

    return sizes, cyk_times, ll_times

def plot(sizes, cyk, ll):
    plt.plot(sizes, cyk, marker='o', label="CYK")
    plt.plot(sizes, ll, marker='o', label="Predictivo LL")

    plt.xlabel("Tamaño de entrada (tokens)")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación de rendimiento: CYK vs LL")
    plt.legend()
    plt.grid()

    plt.show()

if __name__ == "__main__":
    sizes, cyk, ll = measure()
    plot(sizes, cyk, ll)
