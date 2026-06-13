x = float(input("Digite um número: "))
sucessor = x + 1
resultado = x + (3 * sucessor)
print(f"Número digitado: {x}")
print(f"Sucessor do número: {sucessor}")
print(f"Resultado da expressão: {x} + 3 * ({sucessor}) = {resultado}")

if resultado == 74:
    print(f"O número {x} está correto.")
    print("Ele satisfaz a equação.")
else:
    print(f"O número {x} está incorreto.")
    print("Ele não satisfaz a equação.")
    print("O número correto é: 17.75")
