#QUESTÃO02

a = float(input("Quantas maçãs você deseja? na compra de mais de uma duzia a maçã sai por 1 real"))
if a >= 12:
    b = a*1
    print(f'O valor da sua compra é {b} pois você comprou com desconto!')
else:
    print(f'O valor da sua compra é ',a*1.30)