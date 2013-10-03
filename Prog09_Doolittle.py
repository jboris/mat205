__author__ = 'jboris'

from numpy import array, identity
from Prog07_Gauss import leer_matriz_cuadrada, leer_vector, sustitucion as sustitucion_regresiva


def calcular_u_ii(matriz, L, U, i):
    u_ii = matriz[i][i]
    k = 0
    while k <= i-1:
        u_ii -= U[k][i] * L[i][k]
        k += 1
    U[i][i] = u_ii
    return U


def calcular_l_ij(matriz, L, U, i, j):
    l_ij = matriz[i][j]
    k = 0
    while k <= j-1:
        l_ij -= U[k][j] * L[i][k]
        k += 1
    L[i][j] = l_ij / U[j][j]
    return L


def calcular_u_ij(matriz, L, U, i, j):
    u_ij = matriz[i][j]
    k = 0
    while k <= i-1:
        u_ij -= U[k][j] * L[i][k]
        k += 1
    U[i][j] = u_ij
    return U


def doolittle(matriz):
    n = len(matriz)
    L = identity(n)
    U = identity(n)
    i = 0
    while i < n:
        j = 0
        while j < n:
            if i == j:
                U = calcular_u_ii(matriz, L, U, i)
            if i > j:
                L = calcular_l_ij(matriz, L, U, i, j)
            if i < j:
                U = calcular_u_ij(matriz, L, U, i, j)
            j += 1
        i += 1
    return L, U


def sustitucion_progresiva(matriz, vector):
    n = len(matriz)
    x = range(n)
    i = 0
    while i < n:
        suma = vector[i]
        j = 0
        while j < i:
            suma -= x[j] * matriz[i][j]
            j += 1
        x[i] = suma / matriz[i][i]
        i += 1
    return x


def main():
    n = int(raw_input('Grado del sistema: '))
    if n > 1:
        print 'Matriz A'
        A = array(leer_matriz_cuadrada(n))
        print 'Vector b'
        b = array(leer_vector(n))
        L, U = doolittle(A)
        z = sustitucion_progresiva(L, b)
        x = sustitucion_regresiva(U, z)
        print 'Raices'
        print x


if __name__ == '__main__':
    main()