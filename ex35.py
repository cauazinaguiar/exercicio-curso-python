print("-=-"*15)
print("Analisador de Triângulos")
print("-=-"*15)
a=int(input("Digite o primeiro comprimento:"))
b=int(input("Digite o segundo comprimento:"))
c=int(input("Digite o terceiro comprimento:"))
if a<b+c and b<a+c and c<a+b:
    print("Pode formar um triângulo")
else:
    print("Não pode formar um triângulo")