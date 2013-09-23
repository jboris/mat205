__author__ = 'jboris'

ERROR = 1E-6
from cmath import sqrt
#Entradas
n = int(raw_input('Grado:'))
a = []
i = 0
while i <= n:
    mensaje = 'Coef de x^'+str(i)+': '
    coef = float(raw_input(mensaje))
    a.append(coef)
    i += 1
R = float(raw_input('r:'))
S = float(raw_input('s:'))
#Proceso
x = []
while n > 2:
    r = R
    s = S
    er = 1E10
    es = 1E10
    while abs(er) > ERROR and abs(es) > ERROR:
        b = range(len(a))
        b[n] = a[n]
        b[n-1] = a[n-1]+r*b[n]
        i = n - 2
        while i >= 0:
            b[i] = a[i]+r*b[i+1]+s*b[i+2]
            i -= 1
        c = range(len(a))
        c[n] = b[n]
        c[n-1] = b[n-1]+r*b[n]
        i = n - 2
        while i > 0:
            c[i] = b[i]+r*c[i+1]+s*c[i+2]
            i -= 1
        d = c[1]*c[3]-c[2]**2
        dr = (-b[0]*c[3]+b[1]*c[2])/d
        ds = (-b[1]*c[1]+b[0]*c[2])/d
        r += dr
        s += ds
        er = dr/r
        es = ds/s
    x.append((r+sqrt(r**2+4*s))/2)
    x.append((r-sqrt(r**2+4*s))/2)
    n -= 2
    a = b[2:]
if n == 2:
    A = a[2]
    B = a[1]
    C = a[0]
    x.append((-B+sqrt(B**2-4*A*C))/(2*A))
    x.append((-B-sqrt(B**2-4*A*C))/(2*A))
else:
    A = a[1]
    B = a[0]
    x.append(-B/A)
#Salidas
print 'Raices:', x