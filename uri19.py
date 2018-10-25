tempo=int(input(''))


hora = tempo // 3600
tempo = tempo - hora * 3600
minu = tempo //60
segundo = tempo - minu * 60

print('{:.0f}:{:.0f}:{:.0f}'.format(hora,minu,segundo))