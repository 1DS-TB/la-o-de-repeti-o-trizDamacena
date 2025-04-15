numero = int(input("Digite um número: "))
primo = 0 

for i in range(1, numero+1):
    if numero >= 1 and numero % i == 0:
        primo += 1

if primo == 2:
    print(f"{numero} eh primo!")
elif numero < 1 :
    print("INVALIDO")
elif primo >2:
    print(f"{numero} nao eh primo!")
elif primo == 1:
    print("1 nao eh primo")
