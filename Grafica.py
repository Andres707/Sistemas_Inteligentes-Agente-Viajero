import matplotlib.pyplot as plt

def grafica(tipo=0, individuo=None, fitness=None, repeticion=None, ciudades=None, numCiudades=None, textSize=20):
    x = []
    y = []

    if tipo is 0:
        for i in range(numCiudades):
            x.append(ciudades[i][0])
            y.append(ciudades[i][1])

        figCiudades = plt.figure()
        aux = figCiudades.add_subplot(1, 1, 1)
        aux.plot(x, y, "rd")

        for i in range(numCiudades):
            aux.text(x[i], y[i], str(i), fontsize=textSize)
    elif tipo is 1:
        for i in range(numCiudades):
            x.append(ciudades[individuo[i]][0])
            y.append(ciudades[individuo[i]][1])

        figRecorrido = plt.figure()
        aux = figRecorrido.add_subplot(1, 1, 1)
        #plt.title("Individuo: " + str(individuo) + " - Fitness: " + str(fitness))
        plt.title("Fitness: " + str(fitness))
        aux.plot(x, y, "-d", label="Repeticion " + str(repeticion))
        aux.legend(bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0)

        for i in range(numCiudades -1):
            aux.text(x[i], y[i], str(i), fontsize=textSize)
    plt.show()
