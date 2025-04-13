v1 = int(input("Digite o primeiro intervalo: "))
v2 = int(input("Digite o segundo intervalo: "))


for i in range (v1, v2):
    i2 = str(i**2)
    tamanho = len(i2)

    if i < 10:
        if i == 9 or i == 1:
            print(f"O número {i} é um número Kaprekar.")

    elif tamanho % 2 != 0:
        metade = tamanho // 2
        vDireita = tamanho - metade
        vEsquerda = tamanho - vDireita

        direita = int(i2[-vDireita:])
        esquerda = int(i2[:vEsquerda])

        if direita + esquerda == i:
            print(f"O número {i} é um número Kaprekar.")

    else:

        metade = tamanho // 2
        vDireita = tamanho - metade
        vEsquerda = tamanho - vDireita

        direita = int(i2[-vDireita:])
        esquerda = int(i2[:vEsquerda])

        if direita + esquerda == i:
            print(f"O número {i} é um número Kaprekar.")

    metade = 0
    vDireita = 0
    vEsquerda = 0


