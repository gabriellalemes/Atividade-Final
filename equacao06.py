'''

Qual número atende ao seguinte critério? “Sua metade mais 7 é igual a 19.”

'''

numero = 24
resultado = (numero / 2) + 7

print(f"O número correto é {numero}")
print(f"Verificação: metade de {numero} ({numero/2}) + 7 = {resultado}\n")

num_usuario = float(input("Digite um número para comparar: "))
res_usuario = (num_usuario / 2) + 7

if res_usuario == 19:
    print(f"\n✅ Correto! {num_usuario} é o número!")
else:
    print(f"\n❌ Incorreto! O número correto é {numero}")