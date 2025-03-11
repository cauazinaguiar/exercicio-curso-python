salario=float(input("Qual o salário atual?"))
if salario<=1250:
    aumento=salario*(15/100)+salario
    print("O salario aumentou para R${:.2f}".format(aumento))
else:
    aumento=salario*(10/100)+salario
    print("O salário aumentou para R${:.2f}".format(aumento))
