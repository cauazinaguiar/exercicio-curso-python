from random import randint
from time import sleep

comp=randint(0,5)
print("-=-"*20)
print("Eu vou pensar em um número de 0 a 5. Vocẽ consegue advinhar?")
print("-=-"*20)
num=int(input("Digite o número que você acha que eu pensei: "))
print("Processando...")
sleep(2)
if num==comp:
    print("Parabéns, você acertou o número em que eu pensei")
else:
    print("Ihhh, errou. O número em que eu pensei foi {}".format(comp))


