__author__ = 'jboris'

from numpy import array
from Prog07_Gauss import leer_matriz_cuadrada, leer_vector


def gauss_jordan(matriz, vector):
    n = len(matriz)
    i = 0
    while i < n:
        piv = matriz[i][i]
        matriz[i] /= piv
        vector[i] /= piv
        j = i + 1
        while j < n:
            piv = matriz[j][i]
            matriz[j] -= matriz[i] * piv
            vector[j] -= vector[i] * piv
            j += 1
        k = i - 1
        while k >= 0:
            piv = matriz[k][i]
            matriz[k] -= matriz[i] * piv
            vector[k] -= vector[i] * piv
            k -= 1
        i += 1
    return vector


def main():
    n = int(raw_input('Grado del sistema: '))
    if n > 1:
        print 'Matriz A'
        A = array(leer_matriz_cuadrada(n))
        print 'Vector b'
        b = array(leer_vector(n))
        x = gauss_jordan(A, b)
        print 'Raices'
        print x

if __name__ == '__main__':
    main()