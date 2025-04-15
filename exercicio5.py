numero = int(input("Digite um número: "))
primo = 0 
if numero > 1:
    for i in range(1, numero+1):
        if numero >= 1 and numero % i == 0:
            primo += 1

else:
    print("INVALIDO")

