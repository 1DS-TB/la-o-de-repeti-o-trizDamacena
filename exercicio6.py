v1 = int(input("Digite o primeiro intervalo: "))

anterior = 0
atual = 1
proximo = 1
lista = []
if v1 < 1 :
    print("INVALIDO")
else:
    for i in range(1, v1):
        lista.append(anterior)
        proximo = atual + anterior
        anterior = atual
        atual = proximo

lista.append(anterior)
print(lista)
