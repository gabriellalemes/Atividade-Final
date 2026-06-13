'''
“Multiplique um número por 3 e subtraia 9. O resultado é igual ao próprio número.”
Qual é esse número?
'''

num_usuario = float(input("Digite um número para comparar: "))
numero = 4.5
resultado = (3 * numero) - 9

print(f"O número correto é {numero}")
print(f"Verificação: (3 × {numero}) - 9 = {resultado}\n")

res_usuario = (3 * num_usuario) - 9

if res_usuario == num_usuario:
    print(f"\n✅ Correto! {num_usuario} é o número!")
else:
    print(f"\n❌ Incorreto! {num_usuario} não é o número correto. O correto é {numero}.")