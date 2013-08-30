__author__ = 'jboris'

ERROR = 1E-6
#Entradas
ec = raw_input('f(x):')
der = raw_input('f\'(x):')
x0 = float(raw_input('x0:'))
#Proceso
f1 = 1E10
while abs(f1) > ERROR:
    f0 = eval(ec, {'x': x0})
    df0 = eval(der, {'x': x0})
    if f0 == 0 or df0 == 0:
        break
    x1 = x0 - f0 / df0
    f1 = eval(ec, {'x': x1})
    x0 = x1
#Salidas
print 'x:', x1