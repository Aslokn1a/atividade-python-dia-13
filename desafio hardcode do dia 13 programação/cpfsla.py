#def checaCPF (CPF):
        #soma = 0
        #for (i=0, i < 9):
        #soma += parseInt(CPF.charAt(i)) * (10 - i);
        #resto = 11 - (soma % 11);
        #if (resto == 10 || resto == 11)
        #    resto = 0;
        #if (resto != parseInt(CPF.charAt(9)))
        #    return false;
        #soma = 0;
        #for (i = 0; i < 10; i ++)
        #soma += parseInt(CPF.charAt(i)) * (11 - i);
        #resto = 11 - (soma % 11);
        #if (resto == 10 || resto == 11)
        #   resto = 0;
        #if (resto != parseInt(CPF.charAt(10)))
         #   return false;
       
#    return true;
 
def checa(a):
    soma =0
    for i in range(9):
        soma+=int(str(a[i]))*(10-i)
    resto=11-(soma%11)
    print(resto)
    
    if resto ==10 or resto ==11:
        resto = 0
        
    elif resto!=int(str(a[9])):
        print(int(str(a[9])))
        return False
    soma = 0
    for i in range(10):
        soma+=int(str(a[i]))*(11-i)
    resto=11-(soma%11)
    if resto ==10 or resto ==11:
        resto = 0
        
    elif resto!=int(str(a[10])):
        print(int(str(a[10])))
        return False
    return("é cpf")
    print(resto)
print(checa("34485861023"))