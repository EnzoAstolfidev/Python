def real_para_peso(real):
    return real * 7.5

real = float(input("quantos reais voce quer converter?"))
peso = real_para_peso(real)
print(f"R${real} = U${peso}")