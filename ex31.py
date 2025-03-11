distancia=float(input("Digite a distância da viagem que vai percorrer (em Km)"))
print("Sua viagem é de {:.1f}KM".format(distancia))
if distancia<=200:
    preco1=0.5*distancia
    print("Sua viagem irá custar R${:.2f}".format(preco1))
else:
    preco2=0.45*distancia
    print("Sua viagem irá custar R${:.2f}".format(preco2))