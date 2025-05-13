import os;os.system("clear")
i=15 #15= 00001111
j=22  #22=00010110
y=i&j  # isso  é igual ao E na tabela da verdade
x=i|j  # isso  é igual ao OU na tabela da verdade
print(y)#6= 00000110
print(x)#31=00011111

var = 17
var_right = var >> 1#deslocamento de 1 bit para direita
var_left = var << 2 #deslocamento de 2 bits para a esquerda
print (var, var_left, var_right)

x = 4
y = 1
 
a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2
 
print(a, b, c, d, e, f)
lista=[2,4,3,1,7,6,8,1]
lista.sort()
print(lista)
print(lista.count(1))

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
 
print(c + d + e)
 
print(3e1)

def strange_function(c):
    if(c % 2 == 0):
        c = 20
        return True, c
    return False, c
c = 10
flag = strange_function(2)
if flag:
    print(flag)
print(strange_function(1))
 
def list_sum(lst):
    s = 0
    for elem in lst:
        s += elem
    return s
print(list_sum([5, 4, 3]))

n=3.14159
raio=float(input())
area=n*raio**2
print(f"A={area:.4f}")

def multiply(a, b):
    return a * b
print(multiply(3, 4))    # saídas: 12
def multiply(a, b):
    return
print(multiply(3, 4))    # saídas: None

# Exemplo 1
def wishes():
    print("Meus desejos")
    return "Feliz aniversário!"
 
wishes()    # saídas: Meus desejos
 
 
# Exemplo 2
def wishes():
    print("Meus desejos")
    return "Feliz aniversário!"
 
print(wishes())
 
# saídas: Meus desejos
#          Feliz aniversário!
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False
 
print(is_int(5))
print(is_int(5.0))
print(is_int("5"))
 
def my_function(n):
 print("Eu obtive", n)
 n += 1
 print("Eu tenho", n)


var = 1
my_function(var)
print(var)

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
 
 
def lb_to_kg(lb):
    return lb * 0.4535923
 
 
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
 
    return weight / height ** 2
 
 
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))
'''''''''''''''
estrutura base para matriz:
m=[]
for l in range(3):
    linha=[]
    for c in range(3):
        linha.append(int(input("dgt n: ")))
    m.append(linha)
for l in range(3):
    for c in range(3):
        print(m[l][c],end=" ")
    print()
'''
tuple=(1,2,4,5)
tuple1=1,2,3,4,5
print(tuple)
print(tuple1)
my_tuple = (1, 10, 100, 1000)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])
for elem in my_tuple:
    print(elem)
print(sum(tuple1))
print(min(tuple1))
var = 123
t1 = (1, )
t2 = (2, )
t3 = (3, var)
t1, t2, t3 = t2, t3, t1
print(t1, t2, t3)
school_class = {}

while True:
 name = input("Digite o nome do aluno: ")
 if name == '':
  break
 
 score = int(input("Insira a pontuação do aluno (0-10): "))
 if score not in range(0, 11):
  break
 
 if name in school_class:
  school_class[name] += (score,)
 else:
  school_class[name] = (score,)
 
for name in sorted(school_class.keys()):
 adding = 0
 counter = 0
 for score in school_class[name]:
  adding += score
  counter += 1
 print(name, ":", adding / counter)

value=float(input('dgt:'))
type(value) is int

try:
 print(int(9))
 # Esse é um lugar
 # que você pode fazer algo
 # sem pedir permissão.
except:
 print(int(9))
 # Esse lugar é dedicado
 # apenas para implorar por persão.

#primeiro, começando com a palavra-chave try - este é o lugar onde você coloca o código que você suspeita ser arriscado e pode ser encerrado em caso de erro; Nota: esse tipo de erro é chamado de exceção, enquanto a ocorrência da exceção é lançada- podemos dizer que uma exceção é (ou foi) gerada;
#segundo, a parte do código que começa com a palavra-chave except é projetada para lidar com a exceção; depende de você o que você quer fazer aqui: você pode limpar a bagunça ou apenas varrer o problema para baixo do tapete (embora prefiramos a primeira solução).
#Então, poderíamos dizer que esses dois blocos funcionam assim:

#a palavra-chave try marca o local onde você tenta fazer algo sem permissão;
#a palavra-chave except inicia um local onde é possível exibir talentos de desculpas.
