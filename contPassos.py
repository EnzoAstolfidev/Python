#declarar uma variavel e pegar o numero de passos q a pessoa quer dar no dia
#declarar uma variavel para contar passos

#enquanto a variavel de contagem for maior q o objetivo
    #peça para a pessoa digitar quantos passos ela deu ate agora
    #soma passos ate o momento com os passos que ela digitou que deu
    #mostra para a pessoa quantos passos ela deu e quanto ela precisa para atingir o goal

#mostra uma mensagem de parabens

Goal = input("digite quantos passos voce quer dar hoje:\n")
Contagem = 0
contaPassos = input("quantos passos voce deu ate agora?:\n")
while Contagem > Goal:

    if contaPassos > Goal:
        print("caminhe mais")
        print(f"voce caminhou {contaPassos}, faltam: {Goal - contaPassos}")
    elif contaPassos < Goal:
        print("parabens")
    
