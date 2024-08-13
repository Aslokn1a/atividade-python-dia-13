import re
def cpf(a):
    if len(a)==14 :
        if a[3] =="." and a[7] =="." and a[11]=="-":
            a= re.sub("[.-]","",a)
            for i in a:
                if i in('1','2','3','4','5','6','7','8','9') and len(a)==11:
                    return ("é cpf ^w^")
                else:
                    return ("não é cpf >:(")
        else:
            return("digitou errado")

    else:
        a= re.sub("[.-]","",a)
        for i in a:
            if i in('1','2','3','4','5','6','7','8','9') and len(a)==11:
                return ("é cpf ^w^")
            else:
                return ("não é cpf >:(")

cpfs = str(input("informe o cpf: "))
print(cpf(cpfs))

