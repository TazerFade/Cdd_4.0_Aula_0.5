n = int(input("Digite seu número\n"
              "Só será permitido número maior que Zero\n"
              "qual o seu número:"))

if n > 0:
    for c in range(1,n+1,1):
        print(c, end=" ")
else:
    print(" Digite um número maior que zero")