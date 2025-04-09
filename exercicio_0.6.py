cont=0
contalt=0

for x in range (10):
    c = int(input("Informe um número: "))
    if c >= 10 and c <= 20:
        cont = cont + 1
    else:
        contalt = contalt + 1
print(f"A quantidade de números de 10 à 20 é de :{cont}")
print(f"A quantidade de números fora da ordem de 10 à 20 é de :{contalt}")
