
#“A diferença entre um número e sua terça parte é 20.”
#Qual é esse número?

x = 30
terca_parte = x / 3
resultado = x - terca_parte
numero = float(input("Digite um número para comparar: "))

if numero == x:
    print(f"\n✅ Correto! {numero} é o número! E Sua terça parte é {terca_parte}. A diferença é {resultado}\n")
else:
    print(f"\n❌ Incorreto! {numero} não é o número correto. O correto é {x}.")
