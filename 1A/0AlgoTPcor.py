#Ex1
1-0.2-0.2-0.2-0.2-0.2


#Ex2
x=2**3.0+4
print(type(x),x)
x=2>=3 or 2**4*5**2//20==20
print(type(x),x)
x=True or 4>3 and 3>4
print(type(x),x)
x=5%3*5
print(type(x),x)
x=not False and False
print(type(x),x)
x=float(2)**3
print(type(x),x)


#Ex3
a=5
b=a+2
a=b
c=a==b
a=10
d=a!=b
print(a==10 and b==7 and c==True and d==True)


#Ex4
import numpy as np
print(np.sqrt(1+np.sqrt(1+np.sqrt(1+1)))>0)
print(np.sqrt(3)/2-np.e/np.pi>0)


#Ex5
a,b,c,d=4,3,2,1
print(a>=b and a>=c and a>=d)


#Ex6
x,y=4,17
t=y
y=x
x=t
print("x=",x,"y=",y)


#Ex7
a,b,c=1,2,3
m=(a+b+c)/3
print("La moyenne de "+str(a)+",",b,"et",c,"vaut",m)


#Ex8
import numpy as np
import matplotlib.pyplot as plt
X=np.linspace(0,5,1000) 
Y=X**(-X)
plt.plot(X,Y)
plt.show()
X=np.linspace(-3,3,1000) 
Y=X**2
plt.plot(X,Y)
plt.show()
X=np.linspace(-3,3,1000) 
Y=X**3
plt.plot(X,Y)
plt.show()
X=np.linspace(-3,3,1000) 
Y=np.abs(X)
plt.plot(X,Y)
plt.show()
X=np.linspace(0,5,1000) 
Y=np.sqrt(X)
plt.plot(X,Y)
plt.show()
X=np.linspace(-2,2,1000) 
Y=1/X
plt.plot(X,Y)
plt.show()


#Ex9
poids,taille=421,1.10
imc=poids/taille**2
if imc>25:
    print("surpoids")
elif imc<18:
    print("sous-poids")

    
#Ex10
a,b=True,False
if a:
    non_a=False
else:
    non_a=True
if a:
    a_et_b=b
else:
    a_et_b=False
if a:
    a_ou_b=True
else:
    a_ou_b=b

    
#Ex11
x,y,z=1,1,3
if x==y or y==z or x==z:
    print('il y en a deux égaux')
else:
    print('ils sont tous distincts')


#Ex12
a,b,c=1,2,3
if a<b:
    if a<c:
        d=a
    else:
        d=c
else:
    if b<c:
        d=b
    else:
        d=c

        
#Ex13
a,b,c=1,2,3
if a<b:
    if a<c:
        if b<c:
            t=[a,b,c]
        else:
            t=[a,c,b]
    else:
        t=[c,a,b]
else:
    if b<c:
        if a<c:
            t=[b,a,c]
        else:
            t=[b,c,a]
    else:
        t=[c,b,a]

        
#Ex14
x,N=2,5
s=0
y=1
for i in range(N):
    s=s+y
    y=y*x
print(s)


#Ex15
for i in range(100):
    print((i+1)**2-i**2)
    

#Ex16
s1=0
for i in range(101):
    s1+=i**2
print(s1)

s2=0
for i in range(101):
    for j in range(101):
        s2+=i*j
print(s2)

s3=0
for i in range(101):
    for j in range(i,101):
        s3+=i*j
print(s3)

s4=0
for i in range(101):
    for j in range(i+1):
        s4+=i*j
print(s4)


#Ex17
s1=0
for k in range(1,10001):
    s1+=1/k**2
print(s1-np.pi**2/6)

s2=0
for k in range(10001):
    s2+=(-1)**k/(k+1)
print(s2-np.log(2))

s3=0
for k in range(10001):
    s3+=(-1)**k/(2*k+1)
print(s3-np.pi/4)


#Ex18
n=74
s=0
for i in range(n+1):
    s+=i**3
if s==n**2*(n+1)**2/4:
    print("la conjecture est vraie pour n="+str(n))


#Ex19
u=1
for i in range(8):
    u=1/2*(u+2/u)
    print(u)


#Ex20
a,b=1,0
for i in range(2,101):
    c=b
    b=a
    a=a+c
print(a)


#Ex21 (prend 4min)
for a in range(1,1000):
    for b in range(a,1000):
        for c in range(b+1,1001):
            if a**2+b**2==c**2:
                print(a,b,c)


#Ex22
s=0
for i in range(10001):
    if i%3==0 or i%5==0:
        s+=i
print(s)


#Ex23
s=0
for i in range(10001):
    if (i%3==0 or i%5==0) and i%15!=0:
        s+=i
print(s)


#Ex24
def forfait(n):
    pA=1.2*n
    print("Le prix payé avec le forfait A serait de",pA,"euros.")
    pB=20
    print("Le prix payé avec le forfait A serait de",pB,"euros.")
    if pA<pB:
        return "Le forfait le plus favorable est le forfait A"
    else:
        return "Le forfait le plus favorable est le forfait B"
print(forfait(10))
print(forfait(30))


#Ex25
def absolue(n):
    if n>=0:
        return n
    else:
        return -n

def fact(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p

def puissance(x,n):
    p=1
    for i in range(n):
        p*=x
    return p


#Ex26
def max2(a,b):
    if a>=b:
        return a
    else:
        return b

def max3(a,b,c):
    return max2(max2(a,b),c)


#Ex27
def f(u):
    if u%2==0:
        return u//2
    else:
        return 3*u+1
def tps(u):
    n=0
    while u>1:
        u=f(u)
        n+=1
    return n
print(tps(15))
print(tps(127))

#Ex28
max=1
i=1
for u in range(1,1000001):
    t=tps(u)
    if t>max:
        max=t
        i=u
print(i,"a un temps de vol égal à",max)


#Ex29
from numpy.random import randint
def nombre_au_hasard():
    return randint(1,1000)

def juste_prix():
    N=nombre_au_hasard()
    essai=0
    while essai != N: #la condition est vérifiée initialement puisque N est entre 1 et 1000
        essai=int(input("Un nombre entre 1 et 1000 ? "))
        if essai<N:
            print("C'est plus !")
        elif essai>N:
            print("C'est moins !")
    print("Bien joué !")

