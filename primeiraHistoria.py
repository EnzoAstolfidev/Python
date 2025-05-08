print("Acordei na minha xama pela manha, vi o sol nascendo.")
print("oque farei depois?")

choice1 = input("escovarei os dentes ou tomarei banho?").lower()

if(choice1 == "escovarei os dentes"):
    print("AH, meu halito esta bem melhor.")
    choice2 = input("irei tomar um chimas ou comer uma torrada?").lower()
    if(choice2 == "tomar um chimas"):
        print("estava muito bom")
    elif(choice2 == "comer uma torrada"):
        print("estava muito crocante")

elif(choice1 == "tomarei banho"):
    print("me sinto limpinho.")
    choice2 = input("irei tomar um suco ou comer uma polenta?").lower()
    if(choice2 == "tomar um suco"):
        print("estava bem doce")
    elif(choice2 == "comer polenta"):
        print("estava bem suculenta")