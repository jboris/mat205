__author__ = 'jboris'

ERROR = 1E-6
#Entradas
ec = raw_input('f(x):')
x0 = float(raw_input('x0:'))
x1 = float(raw_input('x1:'))
#Proceso
f0 = eval(ec, {'x': x0}) #f(x0)
f1 = eval(ec, {'x': x1}) #f(x1)
f2 = 1E10
if f0 * f1 < 0:
    while abs(f2) > ERROR:
        x2 = (x0 + x1) / 2
        f2 = eval(ec, {'x': x2}) #f(x2)
        if f1 * f2 < 0:
            x0 = x2
        if f0 * f2 < 0:
            x1 = x2
    respuesta = {'x': x2}
else:
    respuesta = 'Datos incorectos'
#Salidas
print respuesta