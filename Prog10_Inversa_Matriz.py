__author__ = 'jboris'

from numpy import array, identity, dot
from Prog07_Gauss import leer_matriz_cuadrada, leer_vector
from Prog08_Gauss_Jordan import gauss_jordan


def inversa(matriz):
    n = len(matriz)
    identidad = identity(n)
    matriz_inversa = gauss_jordan(matriz, identidad)
    return matriz_inversa


def main():
    n = int(raw_input('Grado del sistema: '))
    if n > 1:
        print 'Matriz A'
        A = array(leer_matriz_cuadrada(n))
        print 'Vector b'
        b = array(leer_vector(n))
        A_inversa = inversa(A)
        x = dot(b, A_inversa)
        print 'Raices'
        print x


if __name__ == '__main__':
    main()