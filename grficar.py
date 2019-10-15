__author__ = 'Andres Julian'

import matplotlib.pyplot as plt


def Graficar(listaciudades, persona, secuencia, fitnes):
    x = []
    for i in range(25):
        x.append(listaciudades[persona[i]][0])
    y = []
    for i in range(25):
        y.append(listaciudades[persona[i]][1])
    plt.grid()
    plt.plot(x, y, '-', linewidth=2, color='g')
    plt.plot(x, y, 'o', linewidth=3, color=(0.2, 0.1, 0.4))
    plt.xlabel('x')
    plt.ylabel('y')
    secuencia = str(secuencia)
    fitnes = str(fitnes)
    plt.title('Camino Sugerido, Repeticion: ' + secuencia + ' Fitness: '+ fitnes)
    plt.show()
