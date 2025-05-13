import os;os.system("clear")
def factorial_function(n):
    if n < 0:
        return None
    
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product
for n in range(1,6):  # o n ao mesmo tempo q é os items dentro da lista, tbm define o range la no product 
    print(n, factorial_function(n))
#QP1:
m=[["mat"], ["hist"], ["filo"]]  
som=0
s=0
for l in range(3):
    nota1 = float(input(f"Digite a 1ª nota de {m[l][0]}: "))
    nota2 = float(input(f"Digite a 2ª nota de {m[l][0]}: "))
    freq = float(input(f"Digite o percentual de frequência de {m[l][0]}: "))
    
    # Adiciona as informações à sublista correspondente
    m[l].append(nota1)
    m[l].append(nota2)
    m[l].append(freq)
for l in range(3):
    for c in range(4):
        print(m[l][c], end=" ")
    print()
for l in range(3):
    for c in range(2,3):
        som=som+m[l][2]
for l in range(3):
    for c in range(3,4):  
        s+=m[l][3]      
print(f"mdedia da 1 u={som/3}")
print(f"soma das f={s}")
#● Quantidade de estacionamentos com mais de 200 veículos;
#● O nome do shopping que possui o maior número de veículos registrado;
#● A média de veículos considerando os estacionamentos dos 6 shoppings.
maior_n=0
maior_shopping=""
cout=0
soma=0
for i in range(6):
    name=input("digite o nome do shopping: ")
    total=int(input("digite o total de veículos: "))
    soma+=total
    media=soma/6
    if total>200:
        cout+=1
    if total>maior_n:
        maior_n=total
        maior_shopping=name
print(f"o s com maior n de carro é {maior_shopping}")
print(f"quantidade de s com mais de 200 c é {cout}")
print(f"a média de veículos é {media}")

li=[]
mes=["janeiro","fev","março","abril","maio","junho",
     "julho","agosto","set","out","nov","dezembro"]
for t in range(12):
    temp=float(input(f"digite a media da temperatura no mes {mes[t]}: "))
    li.append(temp)
    somador=sum(li)
    med=somador/12
print("media=",med)
for i in range(12):
    if li[i]>med:
        print(mes[i]," ",li[i])
print(f"a tem mais baixa={min(li)}")

'''''''''''
m=[]
soma=0
maior=0
for l in range(3):
    li=[]
    for c in range(3):
        temp=float(input("dgt a t no ponto e: "))
        li.append(temp)
    m.append(li)
for l in range(3):
    for c in range(3):
        soma+=m[l][c]
        med=soma/9
        print(m[l][c],end=" ")
    print()
for l in range(3):
        if m[l][0]>maior:
            maior=m[l][0]
print(med)
print(maior)
'''''''''
'''''''''''
lista=[]
cout=0
while True:
    voto=int(input("dgt o n do jogador: "))
    if voto==0:
        break
    if 7<=voto<=11:
        lista.append(voto)
        cout+=1
    else:
        print("n inv")
print(f" q d vt vali {cout}")
print("jogador\tvotos\t%")
print(f"7\t{lista.count(7)}\t{(lista.count(7)/cout)*100}%")
print(f"8\t{lista.count(8)}\t{(lista.count(8)/cout)*100}%")
print(f"9\t{lista.count(9)}\t{(lista.count(9)/cout)*100}%")
print(f"10\t{lista.count(10)}\t{(lista.count(10)/cout)*100}%")
print(f"11\t{lista.count(11)}\t{(lista.count(11)/cout)*100}%")
'''''''''
''''''''''
cont=0
somador=0
menormed=999999
menorschool=""
for i in range(5):
    n=input('dgt o nome da school: ')
    media=float(input("dgt a media dos alunos na escola: "))
    somador+=media
    if media>7:
        cont+=1
    if media<menormed:
        menormed=media
        menorschool=n
print(somador,cont,menorschool,sep="  ")
'''''''''
try:
 value = int(input('Digite um número natural: '))
 print('O recíproco de', value, 'é', 1/value) 
except ValueError:
 print('Eu não sei o que fazer.') 
except ZeroDivisionError:
 print('A divisão por zero não é permitida em nosso Universo.') 
    
    
    


        
    







