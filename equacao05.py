'''
"O triplo de um número menos 5 é igual ao dobro do mesmo número mais 1."
Qual é esse número?
'''

numero = 6
lado_esquerdo = (3 * numero) - 5
lado_direito = (2 * numero) + 1

print(f"O número correto é {numero}")
print(f"Verificação: 3×{numero} - 5 = {lado_esquerdo}")
print(f"           2×{numero} + 1 = {lado_direito}\n")

num_usuario = float(input("Digite um número para comparar: "))
eq_esquerda = (3 * num_usuario) - 5
eq_direita = (2 * num_usuario) + 1

if eq_esquerda == eq_direita:
    print(f"\n✅ Correto! {num_usuario} é o número!")
else:
    print(f"\n❌ Incorreto! O número correto é {numero}")