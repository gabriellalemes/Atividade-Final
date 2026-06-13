'''
Qual número atende ao seguinte critério? "Sua metade mais 7 é igual a 19."
'''

num_usuario = float(input("\nDigite um número: "))

resultado = (num_usuario / 2) + 7

print(f"\n📊 {num_usuario}/2 + 7 = {resultado}")

if resultado == 19:
    print(f"\n✅ {num_usuario} é o número correto!")
else:
    print(f"\n ❌ {num_usuario} não é o número correto.")
    print(f" O número correto é 24")
    print(f"   Pois 24/2 + 7 = 12 + 7 = 19")