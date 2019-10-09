import tkinter as tk
from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from time import time
from pip._vendor.distlib.compat import raw_input
import Funciones
import grficar
import threading


class Aplicacion:  # creacion de la ventana
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('400x320')
        self.raiz.configure(bg='beige')
        self.raiz.title('El problema del agente Viajero')
        # ------------------pestañas------------------------------
        tab_control = ttk.Notebook(self.raiz)
        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Inicio')
        tab_control.add(tab2, text='Ciudad')
        tab_control.pack(expand=1, fill='both')
        # ------------------------Label---------------------------
        self.mensajeNC = Label(tab1, text="Numero de ciudades", fg="black")
        self.mensajeNC.pack()
        self.mensajePO = Label(tab1, text="Numero de Individuos", fg="black")
        self.mensajePO.pack()
        self.mensajeRE = Label(tab1, text="Numero de Repeticiones", fg="black")
        self.mensajeRE.pack()
        self.mensajePC = Label(tab1, text="Probabilidad de cruce", fg="black")
        self.mensajePC.pack()
        self.PM = Label(tab1, text="Probabilidad de Mutacion", fg="black")
        self.PM.pack()

        # ------------------------Cajas---------------------------
        self.caja_NC = ttk.Entry(tab1, justify=tk.LEFT)
        self.caja_PO = ttk.Entry(tab1, justify=tk.LEFT)
        self.caja_RE = ttk.Entry(tab1, justify=tk.LEFT)
        self.caja_PC = ttk.Entry(tab1, justify=tk.LEFT)
        self.caja_PM = ttk.Entry(tab1, justify=tk.LEFT)
        # ------------------------Botones---------------------------
        self.botonSA = ttk.Button(tab1, text='Salir', command=self.raiz.destroy).pack(side=BOTTOM)
        self.botonIn = ttk.Button(tab1, text="Iniciar", command=self.algoritmo).pack(side=BOTTOM)
        # ------------------Posicion---------------------------
        self.mensajeNC.place(x=10, y=5)
        self.caja_NC.place(x=10, y=25)
        self.mensajePO.place(x=150, y=5)
        self.caja_PO.place(x=150, y=25)
        self.mensajeRE.place(x=5, y=50)
        self.caja_RE.place(x=10, y=70)
        self.mensajePC.place(x=150, y=50)
        self.caja_PC.place(x=150, y=70)
        self.PM.place(x=10, y=100)
        self.caja_PM.place(x=160, y=100)
        # ------------------------Valores estaticos------------------
        self.caja_NC.insert(0, 13)
        self.caja_PO.insert(0, 1000)
        self.caja_RE.insert(0, 1000)
        self.caja_PC.insert(0, 0.85)
        self.caja_PM.insert(0, 0.01)
        # self.caja_PM.config(state=tk.DISABLED)
        # self.caja_PC.config(state=tk.DISABLED)
        self.raiz.mainloop()

    def caja_texto(self):
        self.raiz = Tk()
        self.raiz.geometry('300x100')
        self.raiz.configure(bg='beige')
        self.raiz.title('cordenadas del punto')
        self.valor = 1
        # ----------------Label--------------------
        self.PX = Label(self.raiz, text="Cordenada X", fg="black")
        self.PX.pack()
        self.PY = Label(self.raiz, text="Cordenada Y", fg="black")
        self.PY.pack()
        self.nota = Label(self.raiz, text="Cordenadas del punto: ")
        self.nota.pack()
        self.numero = Label(self.raiz, text=self.valor)
        self.numero.pack()
        # ----------------Cajas--------------------
        self.caja_PX = ttk.Entry(self.raiz, justify=tk.LEFT)
        self.caja_PY = ttk.Entry(self.raiz, justify=tk.LEFT)
        # ---------------Botones-------------------
        self.boton_sa = ttk.Button(self.raiz, text='Guardar', command=self.puntos).pack(side=BOTTOM)
        # ---------------Posicion------------------
        self.PX.place(x=10, y=25)
        self.PY.place(x=150, y=25)
        self.caja_PX.place(x=10, y=45)
        self.caja_PY.place(x=150, y=45)
        self.nota.place(x=15, y=5)
        self.numero.place(x=150, y=5)
        return 0

    def puntos(self):
        self.numero.config(text=self.valor + 1)
        py = int(self.caja_PY.get())
        px = int(self.caja_PX.get())
        p = [px, py]
        print(p)
        return 0

    def algoritmo(self):
        """ hilo = threading.Thread(target=self.secuencia())
        hilo.start()"""
        # ciudad = self.cafa_texto(self)
        # ----------------0------1----2------3----4------5-----6-----7-----8------9---10-----11---12---13
        listaciudades = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [4, 2], [3, 2], [2, 2], [1, 2],
                         [0, 2], [0, 1]]
        poblacion = int(self.caja_PO.get())
        nr = int(self.caja_NC.get())
        re = int(self.caja_RE.get())
        procruce = float(self.caja_PC.get())
        proMutacion = float(self.caja_PM.get())
        Matriz = []
        Ganadores = []
        start_time = time()
        for m in range(poblacion):
            # agregar comentario
            Matriz.append(Funciones.cadenaN(nr + 1, 0))
        for i in range(poblacion):
            print("Individuo", (i + 1), ": ", Matriz[i])
        # for secuencia in range(re):
        B = True
        # ----------
        secuencia = 0
        # fp = 0
        lim = re
        res = 0
        diferente = 100
        while B:
            fp = 0
            print("Repeticion ", secuencia + 1)
            Fitnes = (Funciones.valoracion(Matriz, poblacion, nr, listaciudades))
            axx = Fitnes.count(0)
            Ganadores = (Funciones.torneo(Fitnes, poblacion))
            probCruce = Funciones.Probabilidad()
            if probCruce > procruce:
                hijos = []
                # print("hijos igual a los padres")
                Ganadores[0] = Ganadores[0] - 1
                Ganadores[1] = Ganadores[1] - 1
                for hj in range(2):
                    hij = Matriz[Ganadores[hj]]
                    hijos.append(hij)
            else:
                hijos = Funciones.cruce(Ganadores, Matriz, nr, 0)
            probMutacion = Funciones.Probabilidad()

            if probMutacion > proMutacion:
                # print("sin mutacion")
                pass
            else:
                for hm in range(2):
                    hijos[hm] = Funciones.mutacion_un_hijo(hijos[hm], nr)
            if Fitnes[fp] < 17:
                Matriz = Funciones.seleccion(Ganadores, hijos, Matriz, nr, listaciudades)
            else:
                FitnesHijos = Funciones.valoracion(hijos, 2, 13, listaciudades)
                Matriz = Funciones.selecciondirecta(Ganadores, hijos, Fitnes, FitnesHijos, Matriz)
            # __________________ OSKAR CHECK ----------------------
            for i in range(poblacion):
                if Fitnes[fp] > Fitnes[i]:
                    fp = i
            if Fitnes[fp] <= 14:
                B = False
            if secuencia == lim:
                res = int(raw_input('Detener ahora? si = 1 no = 2 '))
            if res == 1:
                B = False
            if res == 2:
                lim *= 2
                res = 0
            secuencia += 1
            print('Menor Distancia: ', Fitnes[fp])
            if diferente != Fitnes[fp]:
                diferente = Fitnes[fp]
                grficar.Graficar(listaciudades, Matriz[fp], secuencia, Fitnes[fp])
            else:
                pass

        elapsed_time = time() - start_time
        print("-------------------------Fin-----------------------------------")
        Fitnes = (Funciones.valoracion(Matriz, poblacion, nr, listaciudades))
        Ganador = 0
        libro = open('Ganadores.txt', 'a')
        for i in range(poblacion):
            print("Individuo", (i + 1), ": ", Matriz[i], "Fitnes :", Fitnes[i])
            if Fitnes[Ganador] > Fitnes[i]:
                Ganador = i
            if Fitnes[i] == 0:
                parrafo = "Inividuo", (i + 1), ": ", Matriz[i], "Fitness: ", Fitnes[i]
                parrafo = str(parrafo)
                libro.write('\n' + parrafo)
        libro.write('\n')
        libro.close()

        print("Lapso de tiempo: %.10f segundos." % elapsed_time)
        print("numero de individuaos con un 0: ", axx)
        print("Ganador: ", Ganador + 1)
        print("Ganador: ", Matriz[Ganador], "Fitness: ", Fitnes[Ganador])
        p = "Ganador: ", Matriz[Ganador], "Fitness: ", Fitnes[Ganador]
        p = str(p)
        print("Repeticiones: ", secuencia)
        self.mensajeLT = Label(self.raiz, text="Lapso de tiempo: %.10f segundos." % elapsed_time, fg="black")
        self.mensajeLT.pack()
        self.mensajeG = Label(self.raiz, text=p, fg="black")
        self.mensajeG.pack()
        self.mensajeLT.place(x=10, y=150)
        self.mensajeG.place(x=10, y=190)

        return 0


def main():
    mi_app = Aplicacion()
    return 0


if __name__ == '__main__':
    main()
