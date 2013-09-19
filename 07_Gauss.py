__author__ = 'jboris'


def gauss(matriz, vector):
    n = len(matriz)
    nfilas = 0
    while nfilas < n:
        i = nfilas + 1
        while i < n:
            j = nfilas
            pivote = matriz[i][j]/matriz[nfilas][nfilas]
            while j < n:
                matriz[i][j] -= pivote*matriz[nfilas][j]
                j += 1
            vector[i] -= pivote * vector[nfilas]
            i += 1
        nfilas += 1
    return matriz, vector


def sustitucion(matriz, vector):
    n = len(matriz)
    x = range(n)
    i = 1
    while i <= n:
        suma = vector[n-i]
        j = 1
        while j < i:
            suma -= x[n-j] * matriz[n-i][n-j]
            j += 1
        x[n-i] = suma / matriz[n-i][n-i]
        i += 1
    return x


def leer_matriz_cuadrada(n):
    matriz = []
    nfilas = 0
    while nfilas < n:
        fila = []
        num_elementos = 0
        while num_elementos < n:
            mensaje = 'Elemento[' + str(nfilas+1) + '][' + str(num_elementos+1) + ']: '
            elemento = float(raw_input(mensaje))
            fila.append(elemento)
            num_elementos += 1
        matriz.append(fila)
        nfilas += 1
    return matriz


def leer_vector(n):
    vector = []
    nfilas = 0
    while nfilas < n:
        mensaje = 'Elemento[' + str(nfilas+1) + ']: '
        elemento = float(raw_input(mensaje))
        vector.append(elemento)
        nfilas += 1
    return vector


def mostrar_matriz(matriz):
    alto = len(matriz)
    nfilas = 0
    while nfilas < alto:
        ancho = len(matriz[nfilas])
        num_elementos = 0
        while num_elementos < ancho:
            print matriz[nfilas][num_elementos],
            num_elementos += 1
        print
        nfilas += 1


def main():
    n = int(raw_input('Grado del sistema: '))
    if n > 1:
        A = leer_matriz_cuadrada(n)
        b = leer_vector(n)
        A_mod, b_mod = gauss(A, b)
        x = sustitucion(A_mod, b_mod)
        print 'Raices'
        print x


if __name__ == '__main__':
    main()