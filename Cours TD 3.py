import math,random

var1 = 1.4
var2 = 3
#print(type(var1))
var3=var1*var2
#print("Hello {} Sah {} lol {}".format(var1,var2,var3))
#print(type("Hello"))
#print(int(var2))
#print(float(var2))
#print(var1>var2)
#a= input("Hello")
#print(a)
n=4
if (n%2==0):
    var2=4
    print(var2)
else :
    var1=2.5
    print(var1)
    
for i in range(0,4):
    print(i)

def modifier_non_mutable(a,b):
    a=2*a
    b=3*b


for i in range(0,11):
    print("N° {}".format(i))
    
def Somme(a,b):
    return a+b

print(Somme(12,3))


def ecart(a,b,epsilon=0.1):
    d=math.fabs(a-b)
    if (d<epsilon):
        d=0
    return d

print(ecart(12.2,11.9))

print(math.comb(4,2))
print(math.factorial(9))
print(math.gcd(12345,789))
print(math.lcm(12345,789))