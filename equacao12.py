x = int(input("Digite um número: "))
lado_esquerdo = (4 * x) - 5
lado_direito = (2 * x) + 11
print(f"Lado esquerdo: 4 * {x} - 5 = {lado_esquerdo}")
print(f"Lado direito: 2 * {x} + 11 = {lado_direito}")

if lado_esquerdo == lado_direito:
    print(f"O número que resolve a equação é: {x}")
    print("A solução está correta.")
else:
    print(f"O número {x} não resolve a equação.")
    print("O número correto é: 8")