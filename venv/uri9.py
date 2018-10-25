nome=(input('')).upper()
salario=float(input(''))
venda=float(input(''))
recebe=(venda*0.15)+salario
print('TOTAL = R$ {:.2f}'.format(recebe))