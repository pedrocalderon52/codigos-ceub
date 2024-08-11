def eh_decimal(decimal):
    for char in decimal:
        try:
            int(char)
        except:
            return False
    return True

def eh_binario(binario):
    for char in binario:
        if int(char) not in [0, 1]:
            return False
    return True

def decimal_p_bin():
    binario = input("Digite o número decimal: ")
    if eh_decimal(binario):
        binario = int(binario)
        nums = []
        resto = 9
        quociente = 9
        resultado = ""
        while quociente >= 2:
            quociente = round((binario-0.1)/2)
            resto = binario % 2
            nums.append(resto)
            binario = quociente
        nums.append(1)
        for num in reversed(nums):
            resultado = resultado + str(num)
        resultado = int(resultado)
        return resultado
    
def bin_p_decimal():
    binario = input("Digite o número binário: ")
    while not eh_binario(binario):
        binario = input("Número Inválido!! Digite o seu número binário: ")

    soma_b = 0
    for i, digito in enumerate(reversed(binario)):
        soma_b += int(digito) * (2 ** i)
    return soma_b


resp = input("Calculadora de conversão de bases!! \nQual deseja transformar? \n [1] Binário para decimal \n [2] Decimal para binário \n\n")
if int(resp) == 1:
    resultado = bin_p_decimal()
elif int(resp) == 2:
    resultado = decimal_p_bin()

print(f"A resposta é {resultado}")

