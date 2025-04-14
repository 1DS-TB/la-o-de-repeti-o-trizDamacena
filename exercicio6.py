vezes = int(input("Digite o número: "))
anterior = 0
atual = 1
proximo = 1
lista = [0]

for i in range(1, vezes):
    proximo = atual + anterior
    anterior = atual
    atual = proximo
    lista.append(atual)
if vezes < 1:
    print("INVALIDO")
print(lista)
























