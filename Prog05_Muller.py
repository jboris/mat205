__author__ = 'jboris'

ERROR = 1E-6
#Entradas
ec = raw_input('f(x):')
x0 = float(raw_input('x0:'))
x1 = float(raw_input('x1:'))
x2 = float(raw_input('x2:'))
#Proceso
f3 = 1E10
while abs(f3) > ERROR:
    f0 = eval(ec, {'x': x0})
    f1 = eval(ec, {'x': x1})
    f2 = eval(ec, {'x': x2})
    h0 = x1 - x0
    h1 = x2 - x1
    r0 = (f1 - f0) / h0
    r1 = (f2 - f1) / h1
    a = (r1 - r0) / (h1 + h0)
    b = a * h1 + r1
    c = f2
    from cmath import sqrt
    divisor_pos = b + sqrt(b ** 2 - 4 * a * c)
    divisor_neg = b - sqrt(b ** 2 - 4 * a * c)
    if abs(divisor_pos) > abs(divisor_neg):
        divisor = divisor_pos
    else:
        divisor = divisor_neg
    x3 = x2 + (-2 * c) / divisor
    f3 = eval(ec, {'x': x3})
    x0 = x1
    x1 = x2
    x2 = x3
#Salidas
print 'x:', x3
