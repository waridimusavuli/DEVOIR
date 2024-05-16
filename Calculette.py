nb1=int(input ("entrez un nombre"))
nb2=int(input("entrez un nombre"))
symbole=input("choisir votre symbole")
reponse=nb1+nb2
match symbole:
    case "+":
        reponse=nb1+nb2
        print(reponse)
    case "-":
        reponse=nb1-nb2
        print(reponse)
    case "*":
        reponse=nb1*nb2
        print(reponse)
    case "/":
        reponse=nb1/nb2
        print(reponse)
    case _:
        print("signe non reconnu")
