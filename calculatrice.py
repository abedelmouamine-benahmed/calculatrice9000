def calcule(nb1,operation,nb2):
    
    try:
        if operation=='+':
            resultat= float(nb1)+float(nb2)
            return resultat    
        elif operation=='*':
            resultat=float(nb1)*float(nb2)
            return resultat
        
        elif operation=='-':
            resultat=float(nb1)-float(nb2)
            return resultat
        
        elif operation =='/':
            resultat=float(nb1)/float(nb2)
            return resultat   
        else:
            print("désolé, il y a une erreur dans votre opérateur. Opérateurs autorisés : + - / * ")
    
    except ValueError:
        print("désolé, je ne peux caculer uniquement des chiffres ou des nombres")
    
    except ZeroDivisionError:
        print("erreur division par zéro")

historique1=[]

def historique():
    while True:
        
        voir_historique=input("Voulez-vous voir l'historique o/n: ")
        if voir_historique=='o':
            print(historique1)
            break
        elif voir_historique=='n':
            break
        else:
            print("je n'ai pas compris ")  


def saisi():
    nb1=input('saisir un nombre ou chiffre: ')
    operation=input('saisir une opération: ')
    nb2=(input('saisir un nombre ou chiffre: '))
    historique1.append(calcule(nb1,operation,nb2))
    print(calcule(nb1,operation,nb2))
    return historique()



saisi()

while True :
    continuer=input('Voulez-vous continuer o/n: ')
    
    if continuer=='o' :
        saisi()
       
    elif continuer=='n':
        print("Au revoir \U0001F44B ")
        break
    else:
        print("je n'ai pas compris: ")
    
    
        