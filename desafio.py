saldo = 0

def Mostra_Saldo():
    print(saldo)


def criar_conta():
    Nome = input("qual é seu nome? ")
    idade = int(input("quantos anos voce tem? "))
    if idade < 18:
        print("voce nao tem idade para ter uma conta ")
    elif idade > 18:
        print("voce pode ter uma conta ")
        
    return Nome

def depositar():
    global saldo
    deposito = float(input("quanto voce quer depositar? "))
    if deposito < 1000:
        saldo = saldo + deposito
        print("agora voce possui ", saldo)
    elif deposito > 1000:
        print("voce so pode depositar 1000 reais " )
    return saldo

def sacar():
    global saldo
    saque = float(input("quanto voce quer sacar? "))
    if saque < 1000:
        saldo = saldo - saque
        print("agora voce tem ", saldo)
    elif saque > 1000:
        print("voce so pode sacar 1000 reais ")
    return saldo

def banco():
    Mostra_Saldo()
    conta = criar_conta()

    if conta is None:
        return
    
    while True:
        print("-- menu principal Banco Banrinorte --")
        print("1 - sacar")
        print("2 - depositar")
        print("3 - sair")
        opcao = int(input("escolha uma opção: "))
        
        if opcao == 1:
            sacar()
        elif opcao == 2:
            depositar()
        
banco()
