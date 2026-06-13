x = int(input("Digite um número: "))

lado_esquerdo = (5 * x) + 2
lado_direito = 7 * x


print(f"Lado esquerdo: 5 * {x} + 2 = {lado_esquerdo}")
print(f"Lado direito: 7 * {x} = {lado_direito}")

if lado_esquerdo == lado_direito:
    print(f"O número que resolve a equação é: {x}")
    print("A solução está correta.")
else:
    print(f"O número {x} não resolve a equação.")
    print("O número correto é: 1")
