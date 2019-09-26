import matplotlib.pyplot as plt


def Graficar(listaciudades, persona):
    x = []
    for i in range(15):
        x.append(listaciudades[persona[i]][0])
    y = []
    for i in range(15):
        y.append(listaciudades[persona[i]][1])

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Camino Sugerido ')
    plt.show()
