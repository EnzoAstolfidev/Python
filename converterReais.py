def converter_reais(nome_moeda, valor):
    if moeda == "euro:":
        return valor * 0.16
    elif nome_moeda == "dolar":
        return valor * 0,18
    else:
        return 0.0
    


print("......... convertor de moedas ......")
moeda = input("digite para qual moeda voce quer converter: ")
valor = input("Insira a quantidade de reais brasileiros que voce quer converter")