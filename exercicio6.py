v1 = int(input("Digite o primeiro intervalo: "))
v2 = int(input("Digite o segundo intervalo: "))
anterior = 0
atual = 1
proximo = 1
lista = []
if v1 < 1 or v2 < 1:
    print("INVALIDO")
else:
    for i in range(v1, v2):
        lista.append(anterior)
        proximo = atual + anterior
        anterior = atual
        atual = proximo

lista.append(anterior)
print(lista)






















