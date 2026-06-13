numero = int(input("Digite um numero: "))

lado_esquerdo = (4 * numero) + 10
lado_direito = (3 * numero) + 22

print("Verificação:")
print(f"Lado esquerdo: 4 * {numero} + 10 = {lado_esquerdo}")
print(f"Lado direito: 3 * {numero} + 22 = {lado_direito}")

if lado_esquerdo == lado_direito:
    print(f"O número {numero} está correto.")
    print("Ele satisfaz a equação.")
else:
    print(f"O número {numero} está incorreto.")
    print("Ele não satisfaz a equação.")
    print("O número correto é 12.")
