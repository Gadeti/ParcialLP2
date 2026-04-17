import time

class ParserLL:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def match(self, token):
        if self.pos < len(self.tokens) and self.tokens[self.pos] == token:
            self.pos += 1
        else:
            raise Exception("Error sintáctico")

    def E(self):
        self.T()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ["+", "-"]:
            self.match(self.tokens[self.pos])
            self.T()

    def T(self):
        self.F()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ["*", "/"]:
            self.match(self.tokens[self.pos])
            self.F()

    def F(self):
        if self.tokens[self.pos] == "(":
            self.match("(")
            self.E()
            self.match(")")
        else:
            self.match("num")

    def parse(self):
        self.E()
        return self.pos == len(self.tokens)

def run_example():
    tokens = ["num", "-", "num", "*", "num", "/", "num"]

    start = time.time()
    parser = ParserLL(tokens)
    result = parser.parse()
    end = time.time()

    print("Entrada:", " ".join(tokens))
    print("Resultado:", "ACEPTADA" if result else "RECHAZADA")
    print(f"Tiempo: {end - start:.6f} s")

if __name__ == "__main__":
    run_example()
