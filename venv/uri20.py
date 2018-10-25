idade=int(input(''))
ano=idade//365
meses=(idade %365)//30
dias=(idade %365)%30
print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))