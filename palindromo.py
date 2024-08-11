def eh_palindromo(string):
    string_invertida = []
    j = 0
    for i in range(len(string), 0, -1):
        string_invertida[j] = string[i]
        j+=1
    if string_invertida == string:
        return True
    else: 
        return False

#currently not working

    
    

if eh_palindromo(input("digite uma string e veremos se ela é um palíndromo: ")):
    print("é palindromo")
else:
    print("n é palindromo")


