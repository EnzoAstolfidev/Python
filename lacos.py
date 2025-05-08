#for i in range (11):
#   print(i)

#nom = ["arthur", "diogo", "enzo", "lorenzo", "rafael"]

#for name in nom:
 #   print(name)

#numeros = [1,2,3,4,5,6,7,8,9,10]

#for number in numeros:
   # print(number)



#pegar uma frase e salvar em uma variavel
frase = input("digite aqui uma frase\n").lower()
#declarar uma variavel para contar as vogais
contaVogais = 0
#percorrer a frase
for vogal in frase:
# se a frase.lower() tiver aeiou
    if vogal.lower() in 'aáeéiou':
# somar +1 na variavel que conta
        contaVogais = contaVogais+1
#mostra o seguinte: a frase x tem x vogais
print(f"a frase {frase} tem {contaVogais} vogais.")