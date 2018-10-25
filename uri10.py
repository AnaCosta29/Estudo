cod1,np1,vu1=(input('')).split()
cod2,np2,vu2=(input('')).split()
cod1=int(cod1)
np1=int(np1)
vu1=float(vu1)
############
cod2=int(cod2)
np2=int(np2)
vu2=float(vu2)

pagar=((vu1*np1)+(vu2*np2))
print('VALOR A PAGAR: R$ {:.2f}'.format(pagar))