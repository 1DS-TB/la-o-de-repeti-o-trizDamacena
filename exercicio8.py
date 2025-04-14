N = int(input("Digite um numero: "))
n = 1
soma = 0 
fracoes = []
if N < 0:
    print("INVALIDO")
else:
    while n <= N:
        fracoes.append(n)
        fracao = 1/n
        soma +=fracao
        n +=1
    print(f"{soma:.2f}")