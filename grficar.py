import matplotlib.pyplot as plt

listaciudades = [[0,0], [1,0], [2,0], [3,0], [4,0], [5,0], [5,1], [5,2], [4,2], [3,2], [2,2], [1,2], [0,2], [0,1]]

persona = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0]
x = []
for i in range(15):
    x.append(listaciudades[persona[i]][0])
y = []
for i in range(15):
    y.append(listaciudades[persona[i]][1])

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Camino Sugerido ')
plt.show()