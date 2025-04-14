vezes = int(input("Digite o número: "))
anterior = 0
atual = 1
proximo = 1
lista = []
if vezes < 1:
    print("INVALIDO")
else:
    for i in range(1, vezes):
        lista.append(anterior)
        proximo = atual + anterior
        anterior = atual
        atual = proximo

print(lista)























