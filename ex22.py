nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando o seu nome...")
print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))
print("seu nome tem {} letras".format(len(nome)-nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))
separado=nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separado[0], len(separado[0])))



