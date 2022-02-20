def contem_maiuscula(senha):
    if any(i.isupper() for i in senha):
        return True
    else:
        return False

def contem_minuscula(senha):
    if any(i.islower() for i in senha):
        return True
    else:
        return False

def contem_especial(senha):
    if senha[i] == "!" or "@" or "#" or "$" or "%" or "^" or "&" or "(" or ")" or "*" or "-" or "+":
      return True
    else:
        return False

def contem_digito(senha):
    if senha[i] == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
       return True
    else:
        return False
    



senha = input("Digite sua senha: ")         

senha = list(senha)

i = 0

if len(senha) >= 6:
    if contem_maiuscula(senha) and contem_minuscula(senha) and contem_especial(senha) and contem_digito(senha) == True:
        print ("Sua senha atende todos os requisitos!")
    else:
        print ("Sua senha é fraca. Reveja os requisitos.")
else:
    print("Na sua senha faltam", 6 - len(senha), "caracteres")
