__author__ = 'jboris'

ERROR = 1E-6
#Entradas
ec = raw_input('f(x):')
x0 = float(raw_input('x0:'))
x1 = float(raw_input('x1:'))
#Proceso
f2 = 1E10
while abs(f2) > ERROR:
    f0 = eval(ec, {'x': x0})
    f1 = eval(ec, {'x': x1})
    x2 = x1 - (f1 * (x1 - x0)) / (f1 - f0)
    f2 = eval(ec, {'x': x2})
    x0 = x1
    x1 = x2
#Salidas
print 'x:', x2