n = int(input("Digite um número: "))
if n < 1:
    print("INVALIDO")

for linha in range(1, n+1):
    for x in range(linha):
        print("x ", end=" ")
    print()
