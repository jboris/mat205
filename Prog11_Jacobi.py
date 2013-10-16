__author__ = 'jboris'

from numpy import array, zeros, dot, absolute
from numpy.linalg import norm
from Prog07_Gauss import leer_matriz_cuadrada, leer_vector
from Prog10_Inversa_Matriz import inversa

ERROR = 1E-6


def jacobi(A, b, x0):
    n = len(A)
    C = zeros((n, n))
    D = zeros((n, n))
    i = 0
    while i < n:
        j = 0
        while j < n:
            if i == j:
                D[i][i] = A[i][i]
            else:
                C[i][j] = A[i][j]
            j += 1
        i += 1
    D_inversa = inversa(D)
    M = -dot(D_inversa, C)
    n = dot(D_inversa, b)
    er = 1E10
    while er > ERROR:
        x1 = dot(M, x0) + n
        er = norm(x0-x1)
        x0 = x1
    return x1


def main():
    n = int(raw_input('Grado del sistema: '))
    if n > 1:
        print 'Matriz A'
        A = array(leer_matriz_cuadrada(n))
        print 'Vector b'
        b = array(leer_vector(n))
        print 'Vector x0'
        x0 = array(leer_vector(n))
        x = jacobi(A, b, x0)
        print 'Raices'
        print x


if __name__ == '__main__':
    main()