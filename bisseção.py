import os;os.system('clear')
print('seu objetivo é achar as raizes(y=0 da função) abaixo')
print('f(x)=x³+x²-2x')
print('digite +0 para o programa')
while True:
    x1=float(input('digite um valor para x: '))
    f1=(x1**3)+(x1**2)-2*x1
    x2=float(input('digite outro valor para x: '))
    f2=(x2**3)+(x2**2)-2*x2
    x_novo=(x1+x2)/2
    f3=(x_novo**3)+(x_novo**2)-2*x_novo
    if x1==+0 or x2==+0:
        break
    print(f'\n a imagem da função quando x igual a {x1} resulta em y= {f1}')
    if f1==0:
        print('você achou a raiz da função')
    print(f' a imagem da função quando x igual a {x2} resulta em y= {f2}')
    if f2==0:
        print('você achou a raiz da função')
    if f1>0 and f2<0 or f1<0 and f2>0:
        print(f'\n pelo menos existe uma raiz nesse intervalo de {x1} ate {x2}')
    else:
        print(f'\n não existe uma raiz nesse intervalo de {x1} ate {x2}')
    print(f'\n a média aritmética dos x é igual a {x_novo} a qual resulta em y= {f3}')
    if f3==0:
        print('você achou a raiz da função')
    else:
        print('\nprossiga comparando aos valores anteriores')
    
    
