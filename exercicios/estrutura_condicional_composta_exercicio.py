
# Tratamento de notas inválidas

# Condicional composta, entrada pelo usuário

nota = float(input("Qual a sua nota?: "))

if nota <= 0 or nota > 10:
    print("erro:Erro inválidade. Digite um valor entre 0 e 10.")

elif nota >= 9:
    print("Aprovado")

elif nota >= 7:
    print("Recuperação")

else: 
    print("Reprovado")
