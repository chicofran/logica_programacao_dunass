nota1= float(input("Digite a nota do aluno: "))
nota2= float(input("Digite a nota do aluno: "))

media = (nota1 + nota2) / 2
print("A média do aluno é: ", media)

if media >= 9:
    print("Aprovado com louvor")
elif media >=8:
    print("Aprovado")
else:
    print("Reprovado")
