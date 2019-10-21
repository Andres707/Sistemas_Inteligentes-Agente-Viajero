import math
import random
from random import shuffle


# DOCUMENTATION: Funcion para ciudades aleatorias
#  dentro del rango del limite de ciudades
def crearCiudades(ciudades):
    listaCiudades = []

    x = [i for i in range(ciudades)]
    y = [i for i in range(ciudades)]

    shuffle(x)
    shuffle(y)

    for i in range(ciudades):
        listaCiudades.append([x[i], y[i]])

    return listaCiudades


# DOCUMENTATION: Funcion para individuos aleatorios
#  con las posiciones de las ciudades
def individuo(ciudades, origen):
    x = [i for i in range(ciudades)]

    shuffle(x)

    for i in range(ciudades):
        if x[i] == origen:
            aux = x[0]
            x[0] = origen
            x[i] = aux
            break

    x.append(origen)

    return x


# DOCUMENTATION: Funcion para calcular el fitness de una poblacion
#  de individuos
def evaluar(poblacion, numIndividuos, ciudades, listaCiudades):
    fitness = []

    for pos in range(numIndividuos):
        _distancia = 0
        _individuo = poblacion[pos]
        for i in range(ciudades):
            _currentC = _individuo[i]
            _nextC = _individuo[i+1]

            _dist = round(math.sqrt((listaCiudades[_currentC][0] - listaCiudades[_nextC][0]) ** 2 +
                                    (listaCiudades[_currentC][1] - listaCiudades[_nextC][1]) ** 2), 2)
            _distancia += _dist

        fitness.append(_distancia)

    return fitness


# DOCUMENTATION: Funcion para obtener 2 padres con seleccion por torneo
def torneo(poblacion, fitness):
    ganadores = []
    _seleccionado = -1

    for i in range(2):
        _isDifferent = False

        while not _isDifferent:
            _cand1 = random.randrange(poblacion)
            _cand2 = random.randrange(poblacion)

            if _cand1 is not _cand2 and _cand1 is not _seleccionado and _cand2 is not _seleccionado:
                _isDifferent = True

        if fitness[_cand1] < fitness[_cand2]:
            ganadores.append(_cand1)
        else:
            ganadores.append(_cand2)
        _seleccionado = ganadores[0]

    return ganadores


# DOCUMENTATION: Funcion de cruce para obtener los 2 hijos a partir de los
#  padres
def cruce(poblacion, posPadres, ciudades):
    hijos = []

    posRandom = random.randrange(ciudades)

    for i in range(2):
        hijo = []
        _places1 = poblacion[posPadres[0]].copy()
        _places2 = poblacion[posPadres[1]].copy()

        if i is 0:
            for j in range(posRandom):
                hijo.append(_places1[j])
                _places2.remove(_places1[j])
            hijo.extend(_places2)
        else:
            for j in range(posRandom):
                hijo.append(poblacion[posPadres[i]][j])
                _places1.remove(_places2[j])
            hijo.extend(_places1)

        hijos.append(hijo)

    return hijos


def mutacion(hijos, ciudades):
    _pos1 = random.randrange(1, ciudades)
    _isDifferent = False

    while not _isDifferent:
        _pos2 = random.randrange(1, ciudades)

        if _pos1 is not _pos2:
            _isDifferent = True

    for i in range(2):
        aux = hijos[i][_pos1]
        hijos[i][_pos1] = hijos[i][_pos2]
        hijos[i][_pos2] = aux


def seleccionDirecta(poblacion, posPadres, fitness, hijos, fitnessHijos):
    mejores = []
    _familia = []
    _fitness = fitness.copy()
    _poblacion = poblacion.copy()
    _fitnessHijos = fitnessHijos.copy()
    _hijos = hijos.copy()

    for i in range(2):
        for j in range(2):
            if i is 0:
                _familia.append([_fitness[posPadres[j]], _poblacion[posPadres[j]]])
            else:
                _familia.append([_fitnessHijos[j], _hijos[j]])

    _familia.sort()

    for i in range(2):
        mejores.append(_familia[i])

    return mejores


def remplazo(poblacion, posPadres, fitness, mejores):
    for i in range(2):
        poblacion[posPadres[i]] = mejores[i][1]
        fitness[posPadres[i]] = mejores[i][0]


def mejor(poblacion, fitness):
    mejor = []
    aux = []
    _poblacion = poblacion.copy()
    _fitness = fitness.copy()

    for i in range(len(poblacion)):
        aux.append([_fitness[i], _poblacion[i], i])

    aux.sort()
    mejor = aux[0]
    return mejor