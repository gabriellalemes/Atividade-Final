'''
Três amigos somaram suas idades. 
João tem o dobro da idade de Pedro. 
Carlos tem a mesma idade de Pedro. 
A soma das idades é 60 anos. Qual é a idade de cada um?
'''

idade_pedro = 15
idade_joao = 2 * idade_pedro
idade_carlos = idade_pedro
soma = idade_joao + idade_pedro + idade_carlos

pedro = float(input("Digite a idade de Pedro para testar: "))

print(f"Idade correta de Pedro: {idade_pedro} anos")
print(f"Idade correta de João: {idade_joao} anos")
print(f"Idade correta de Carlos: {idade_carlos} anos")
print(f"Soma correta: {soma} anos\n")


if pedro == idade_pedro:
    print(f"\n✅ Correto! Pedro = {pedro}, João = {pedro*2}, Carlos = {pedro}")
else:
    print(f"\n❌ Incorreto! O correto é Pedro = {idade_pedro}")