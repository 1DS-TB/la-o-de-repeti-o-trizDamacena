numero = int(input("Digite um número: "))
primo = 0 

for i in range(1, numero+1):
    if numero > 1 and numero % i == 0:
        primo += 1

if primo == 2:
    print(f"{numero} é primo!")
else:
    print(f"o número {numero} não é primo.")
    