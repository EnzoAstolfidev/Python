nota1 = 0
nota2 = 0
nota3 = 0
media = 0


nota1 = float(input("digite a sua primeira nota\n"))
nota2 = float(input("digite a sua segunda nota\n"))
nota3 = float(input("digite a sua terceira nota\n"))

media = (nota1 + nota2 + nota3)/3
if(media>7):
    print("voce esta aprovado\n")
elif(media<5):
    print("voce esta reprovado\n")
elif(media<=7 and media>=5):
    print("voce esta de recuperação\n")




print(f"sua media é{media}")