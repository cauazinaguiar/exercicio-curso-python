velo=int(input("Qual a velocidade do seu carro?"))
if velo<=80:
    print("Ok, velocidade permitida. Dirija com segurança")
else:
    multa=(velo-80)*7
    print("Multado. Você excedeu o limite de velocidade permitido que é de 80Km/h")
    print("Você deve pagar uma multa de R${}!".format(multa))