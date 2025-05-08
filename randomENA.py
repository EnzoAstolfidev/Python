import random

numeroRandomico = random.randint(1,10)
guessed = False
tentativa = 0

print("Bem vindo ao jogo de adivinhação:")
while not guessed:
    guess = int(input("Digite um número"))
    tentativa = tentativa+1
    if(guess<numeroRandomico):
        print("número mais baixo que o randomico, tente de novo")
    elif(guess>numeroRandomico):
        print("número mais alto que o randomico, tente de novo")
    else:
        guessed = True
        print(f"parabéns, voce acertou o número, era o número {numeroRandomico}")
        print(f"você demorou {tentativa} tentativas")