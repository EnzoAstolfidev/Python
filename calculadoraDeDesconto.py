valor = float(input("digite o valor da sua compra: \n"))
tipoUsuario = input("digite o seu tipo de usuario: Comum, Vip ou Premium: \n").lower()

print(valor)
print(tipoUsuario)

if(tipoUsuario == "comum"):
    print("voce não ganha desconto,infelizmente. Assine nossos planos para ter desconto na compra de roupas. \n") 
elif(tipoUsuario == "vip"):
    print("voce ganhou 10 porcento de desconto")
    valor = valor - (valor*0.1)
elif(tipoUsuario == "premium"):
    print("voce ganhou 20 porcento de desconto")
    valor = valor - (valor*0.2)

print(f"O valor final da sua compra ficou: {valor}")