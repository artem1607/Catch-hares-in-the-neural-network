"""'''
a = 1
suma = 0
while a >= 0.000001:
    a = a / 2
    suma += a
suma = suma + (a / 2)
print(suma)

def mysum(k, m):
    return k + m

def mymul(k, m):
    return k * m

print(mysum(mymul(22, 22), mymul(33, 33)))

def fibon(n):
    a = 0
    b = 1
    while a < n:
        print(a, end =' ')
        a, b = b, b + a

print(fibon(1000))

def fact(j):
    mul = 1
    for i in range(1, j + 1):
        mul *= i
    return mul

print(fact(6))

def fact2(t):
    mul = 1
    while t >= 1:
        mul *= t
        t = t - 1
    return mul
print(fact2(8))

s = [5300, 800, 97, 87, 9]
s.sort()
for i in range(len(s)):
    print(s[i], end='\t')

d = 'Кулишкин', 'Артём', 'Владимирович', 16
print(d)
fam, nam, otch, age = d
print(nam)
'''
f = open('workfilee', 'w')
f.write('с++\n')
f.close()
f = open('workfile', 'w')
f.write('программист Петя создал телеграмм бота\n')
f.close()
(xa * xb + ya * yb) / (((xa ** 2 + ya ** 2) ** 0.5) * ((xb ** 2 + yb ** 2) ** 0.5))
(xb - xa) / ((xa ** 2 + ya ** 2) ** 0.5)"""