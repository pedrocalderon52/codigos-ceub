def eh_primo(num):
    divs = 0
    i = 1
    for i in range(num):
        if num % (i + 1) == 0:
            divs +=1
        if divs == 2:
            return True
        else:
            return False
        

n = int(input("Insira um número: "))

if eh_primo(n):
    print(" é primo")
else: 
    print("nao é primo")
