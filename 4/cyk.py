import time

# Gramática en CNF extendida (+, -, *, /)
grammar = {
    "E": [["E", "X"], ["T"]],
    "X": [["OP1", "T"]],
    "OP1": [["+"], ["-"]],

    "T": [["T", "Y"], ["F"]],
    "Y": [["OP2", "F"]],
    "OP2": [["*"], ["/"]],

    "F": [["L", "Z"], ["NUM"]],
    "Z": [["E", "R"]],

    "L": [["("]],
    "R": [[")"]],
    "NUM": [["num"]],
}

def cyk_parse(tokens):
    n = len(tokens)
    table = [[set() for _ in range(n)] for _ in range(n)]

    # Inicialización
    for i in range(n):
        for lhs, rules in grammar.items():
            for rule in rules:
                if len(rule) == 1 and rule[0] == tokens[i]:
                    table[i][i].add(lhs)

    # CYK
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            for k in range(i, j):
                for lhs, rules in grammar.items():
                    for rule in rules:
                        if len(rule) == 2:
                            B, C = rule
                            if B in table[i][k] and C in table[k+1][j]:
                                table[i][j].add(lhs)

    return "E" in table[0][n-1]

def run_example():
    tokens = ["num", "-", "num", "*", "num", "/", "num"]

    start = time.time()
    result = cyk_parse(tokens)
    end = time.time()

    print("Entrada:", " ".join(tokens))
    print("Resultado:", "ACEPTADA" if result else "RECHAZADA")
    print(f"Tiempo: {end - start:.6f} s")

if __name__ == "__main__":
    run_example()
