K = int(input('Digite o número'))
K = K**2
print(K)

tamanho = len(str(K))
print(tamanho)
if tamanho % 2 != 0:
    print('impar')
else:
    print('par')