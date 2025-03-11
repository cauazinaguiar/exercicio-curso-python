nome = str(input("Digite seu nome completo: ")).title().strip()
print("Muito prazer em te conhecer!")
separado= nome.split()
print("seu primeiro nome é {}".format(separado[0]))
print("seu último nome é {}".format(separado[len(separado)-1]))

