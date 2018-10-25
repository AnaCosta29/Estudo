from math import pow
A,B,C=(input('')).split()
A=float(A)
B=float(B)
C=float(C)

pi=3.14159
TRIANGULO=(A*C)/2
CIRCULO=pi*pow(C,2)
TRAPEZIO=(A+B)*C/2
QUADRADO=pow(B,2)
RETANGULO=A*B



print('TRIANGULO: {:.3f}'.format(TRIANGULO))
print('CIRCULO: {:.3f}'.format(CIRCULO))
print('TRAPEZIO: {:.3f}'.format(TRAPEZIO))
print('QUADRADO: {:.3f}'.format(QUADRADO))
print('RETANGULO: {:.3f}'.format(RETANGULO))
