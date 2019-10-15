__author__ = 'Andres Julian'

from random import shuffle
import random
import math


# Probabilida
def Probabilidad():
    ra = round(random.random(), 2)
    return ra


# Poblacion
def cadenaN(numerolimite, origen):
    x = [i for i in range(0, numerolimite)]
    shuffle(x)
    for i in range(numerolimite):
        if x[i] == origen:
            ap = i
    puntorigen = x[0]
    puntofin = x[ap]
    x[ap] = puntorigen
    x[origen] = puntofin
    x.append(x[origen])
    return x


# Valoracion
def valoracion(poblacion, NumeroPoblacion, NumeroAlelos, Lista):
    Valor = []
    contador = 0
    for m in range(NumeroPoblacion):
        matriz = poblacion[m]
        i = 1
        for i in range(NumeroAlelos):
            n = matriz[i]
            n1 = matriz[i + 1]
            r = round(math.sqrt((Lista[n][0] - Lista[n1][0]) ** 2 +(Lista[n][1] - Lista[n1][1]) ** 2), 2)
            contador = contador + r
        Valor.append(contador)
        contador = contador * 0
    return Valor


# torneo
def torneo(valores, poblacion):
    Ganadores = []
    for i in range(2):
        a1 = random.randrange(1, poblacion)
        a2 = random.randrange(1, poblacion)
        bandera = True
        while bandera:
            if a1 == a2:
                a2 = random.randrange(1, poblacion)
                a1 = random.randrange(1, poblacion)
            else:
                bandera = False
        aa1 = valores[a1]
        aa2 = valores[a2]
        if aa1 < aa2:
            Ganadores.append(a1)
        else:
            Ganadores.append(a2)
    return Ganadores


# cruce
def cruce(Ganadores, matriz, nr, origen):
    nr = nr + 1
    hijos = []
    hijo = []
    Ganadores[0] = Ganadores[0] - 1
    Ganadores[1] = Ganadores[1] - 1
    a1 = random.randrange(1, nr)
    ba1 = True
    while ba1:
        if a1 == 0 or a1 == nr:
            a1 = random.randrange(1, nr)
        else:
            ba1 = False
    # print('Alelo donde se segmenta: ',a1)
    ax1 = a1
    for j in range(2):
        for i in range(a1):
            hijo.append((matriz[Ganadores[j]][i]))
        for m in range(nr):
            if j == 0:
                a = hijo.count(matriz[Ganadores[1]][m])
                if a == 0:
                    hijo.insert(ax1, matriz[Ganadores[1]][m])
                ax1 = ax1 + 1
            else:
                a = hijo.count(matriz[Ganadores[0]][m])
                if a == 0:
                    hijo.insert(ax1, matriz[Ganadores[0]][m])
                ax1 = ax1 + 1
        hijo.append(origen)
        hijos.append(hijo)
        hijo = hijo * 0
        ax1 = a1
    return hijos


# mutacion
def mutacion_un_hijo(hijo, nr):
    nr = nr + 1
    r1 = random.randrange(nr)
    r2 = random.randrange(nr)
    br1 = True
    while br1:
        if r1 == 0 or r1 == nr:
            r1 = random.randrange(nr)
        else:
            br1 = False
    br2 = True
    while br2:
        if r2 == 0 or r2 == nr:
            r2 = random.randrange(nr)
        else:
            br2 = False
    for i in range(2):
        G1 = hijo[i][r1]
        G2 = hijo[i][r2]
        hijo[i][r1] = G2
        hijo[i][r2] = G1
    return hijo


# selecion directa
def selecciondirecta(Ppadres, hijos, fitnes, fitneshijos, matriz):
    ax = []
    Ppadres[0] = Ppadres[0] - 1
    Ppadres[1] = Ppadres[1] - 1
    for i in range(2):
        for j in range(2):
            if i == 0:
                ax.append([fitnes[Ppadres[j]], "p" + str(j)])
            else:
                ax.append([fitneshijos[j], "h" + str(j)])
    # print(ax)
    ax.sort()
    # print(ax)
    mejor1 = ax[0]
    mejor2 = ax[1]
    if mejor1[1] == 'h0' or mejor2[1] == 'h0':
        matriz[Ppadres[0]] = hijos[0]
    elif mejor1[1] == 'h1' or mejor2[1] == 'h1':
        matriz[Ppadres[1]] = hijos[1]
    if mejor2[1] == 'p0':
        matriz[Ppadres[1]] = matriz[Ppadres[0]]
    elif mejor1[1] == 'p1':
        matriz[Ppadres[0]] = matriz[Ppadres[1]]
    return matriz


# seleccion
def seleccion(padres, hijos, matriz, nr, lc):
    # Insertar padres e hijos a individuos
    padres[0] = padres[0] - 1
    padres[1] = padres[1] - 1
    dk = []
    individuo = hijos
    for i in range(2):
        individuo.append(matriz[padres[i]])
    valor = valoracion(individuo, 4, nr, lc)  # Fitness
    # Se busca al ganador
    ganador = 0
    contador = 0
    for i in range(4):
        if valor[ganador] > valor[i]:
            ganador = i
    a = 0  # Ganador 2
    for m in range(4):
        x = individuo[ganador]
        if ganador == m:
            dk.append(0)
        else:
            for i in range(nr):
                if x[i] != individuo[m][i]:
                    contador = contador + 1
            dk.append(contador)
        if dk[a] < dk[m]:
            a = m
            # 3 = p2
            # 2 = p1
    if ganador == 3:
        if a == 2 or a == 3:
            pass
        elif ganador == 2:
            matriz[padres[0]] = individuo[a]
    elif ganador == 0 or ganador == 1:
        matriz[padres[0]] = individuo[ganador]
        if a == 0 or a == 1:
            matriz[padres[1]] = individuo[a]
    return matriz


# random cidudad
def ciudades(nc):
    x = [i for i in range(1, nc)]
    y = [i for i in range(1, nc)]
    shuffle(x)
    shuffle(y)
    lista = []
    for i in range(nc - 1):
        lista.append([x[i], y[i]])
    print(lista)

    return lista
