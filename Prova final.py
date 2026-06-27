
nome = input("Nome do aluno: ")
codigo = input("Código da disciplina: ")

print("\nDigite as 6 notas do aluno:")

p1 = float(input("P1: "))
p2 = float(input("P2: "))
pd = float(input("PD: "))
pp1 = float(input("Pp1: "))
pp2 = float(input("Pp2: "))
pp3 = float(input("Pp3: "))

media = (p1 + p2 + pd + pp1 + pp2 + pp3) / 6

if media >= 6.0:
    situacao = "Aluno Aprovado"
elif media >= 4.0:
    situacao = "Aluno em Recuperação"
else:
    situacao = "Aluno Reprovado"

print("Nome do aluno:", nome)
print("Código da disciplina:", codigo)
print(f"Nota Final: {media:.2f}")
print("Situação:", situacao)