num_usuario = float(input("\nDigite um número: "))

resultado = (4 * num_usuario) - 8

if resultado == 28:
    print(f"\n✅ {num_usuario} é o número correto!")
else:
    print(f"\n❌ {num_usuario} não é o número correto.")
    print(f" O número correto é 9")
    print(f"   Pois 4 × 9 - 8 = 36 - 8 = 28")