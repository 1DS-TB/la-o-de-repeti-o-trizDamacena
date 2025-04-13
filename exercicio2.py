N = int(input("Digite um número: "))
soma = 0

if N > 0:
    N += 1
    while N > 1:
        N -= 1
        soma += N

    print(soma)