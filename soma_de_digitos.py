def soma_de_digitos(num):
    soma = 0
    strnum = str(num)
    lista = []
    for i in range(len(strnum)):
        lista.append(int(strnum[i]))
    for j in lista:
        soma += j
    return soma


num = int(input("Insira um número: "))
print(f"a soma de digitos é {soma_de_digitos(num)}")

