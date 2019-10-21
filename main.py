__author__ = 'Andres Julian'
import tkinter as tk
from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from time import time
from pip._vendor.distlib.compat import raw_input
import Funciones
import grficar


# import threading


class Aplicacion:  # creacion de la ventana
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('600x320')
        self.raiz.configure(bg='beige')
        self.raiz.title('El problema del agente Viajero')
        # ------------------pestañas------------------------------
        tab_control = ttk.Notebook(self.raiz)
        ini = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)
        tab_control.add(ini, text='Inicio')
        tab_control.add(tab2, text='Ciudades')
        tab_control.pack(expand=1, fill='both')
        # ------------------------Label---------------------------
        mensajeNC = Label(ini, text="Numero de ciudades", fg="black")
        mensajePO = Label(ini, text="Numero de Individuos", fg="black")
        mensajeRE = Label(ini, text="Numero de Repeticiones", fg="black")
        mensajePC = Label(ini, text="Probabilidad de cruce", fg="black")
        PM = Label(ini, text="Probabilidad de Mutacion", fg="black")
        ori = Label(ini, text="Origen", fg="black")
        des = Label(ini, text="Destino", fg="black")
        # ------------------------Cajas---------------------------
        self.caja_NC = ttk.Entry(ini, justify=tk.LEFT)
        self.caja_PO = ttk.Entry(ini, justify=tk.LEFT)
        self.caja_RE = ttk.Entry(ini, justify=tk.LEFT)
        self.caja_PC = ttk.Entry(ini, justify=tk.LEFT)
        self.caja_PM = ttk.Entry(ini, justify=tk.LEFT)
        self.caja_OR = ttk.Entry(ini, justify=tk.LEFT)
        self.caja_DE = ttk.Entry(ini, justify=tk.LEFT)
        # ------------------------Botones---------------------------
        self.botonSA = ttk.Button(ini, text='Salir', command=self.raiz.destroy).place(x=290, y=250)
        self.botonIn = ttk.Button(ini, text="Iniciar", command=self.algoritmo).place(x=190, y=250)
        # ------------------Posicion---------------------------
        mensajeNC.place(x=10, y=5)
        self.caja_NC.place(x=10, y=25)
        mensajePO.place(x=150, y=5)
        self.caja_PO.place(x=150, y=25)
        mensajeRE.place(x=290, y=5)
        self.caja_RE.place(x=290, y=25)
        mensajePC.place(x=430, y=5)
        self.caja_PC.place(x=430, y=25)
        PM.place(x=8, y=50)
        self.caja_PM.place(x=10, y=70)
        ori.place(x=155, y=50)
        self.caja_OR.place(x=155, y=70)
        des.place(x=290, y=50)
        self.caja_DE.place(x=290, y=70)
        # ------------------------fin--------------------------------
        self.mensajeLT = Label(ini, text=" ", fg="black")
        self.mensajeG = Label(ini, text=" ", fg="black")
        self.mensajeLT.place(x=10, y=150)
        self.mensajeG.place(x=10, y=190)
        # ------------------------Valores estaticos------------------
        self.caja_NC.insert(0, 25)
        self.caja_PO.insert(0, 1000)
        self.caja_RE.insert(0, 10000)
        self.caja_PC.insert(0, 0.85)
        self.caja_PM.insert(0, 0.01)
        self.caja_OR.insert(0, 0)
        self.caja_DE.insert(0, 3)
        self.caja_PM.config(state=tk.DISABLED)
        self.caja_PC.config(state=tk.DISABLED)
        self.raiz.mainloop()

    def algoritmo(self):
        poblacion = int(self.caja_PO.get())
        alelos = int(self.caja_NC.get())
        rep = int(self.caja_RE.get())
        procruce = float(self.caja_PC.get())
        proMutacion = float(self.caja_PM.get())
        origen = int(self.caja_OR.get())
        destino = int(self.caja_DE.get())
        listaciudades = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [4, 2], [3, 2], [2, 2], [1, 2],
                         [0, 2], [0, 1]]
        # Funciones.ciudades(alelos + 2)
        print(listaciudades)
        Matriz = []

        # Ganadores = []
        start_time = time()
        for m in range(poblacion):
            # agregar comentario
            Matriz.append(Funciones.cadenaN(alelos + 1, origen, destino))
        for i in range(poblacion):
            print("Individuo", (i + 1), ": ", Matriz[i])
        # for secuencia in range(re):
        B = True
        # ----------
        secuencia = 0
        # fp = 0
        lim = rep
        res = 0
        diferente = 100
        while B:
            fp = 0
            print("Repeticion ", secuencia + 1)
            Fitnes = (Funciones.valoracion(Matriz, poblacion, alelos, listaciudades))
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
                hijos = Funciones.cruce(Ganadores, Matriz, alelos, destino)
            probMutacion = Funciones.Probabilidad()

            if probMutacion > proMutacion:
                # print("sin mutacion")
                pass
            else:
                hijos = Funciones.mutacion_un_hijo(hijos, alelos)
            if Fitnes[fp] < 14:
                Matriz = Funciones.seleccion(Ganadores, hijos, Matriz, alelos, listaciudades)
            else:
                hijos = Funciones.mutacion_un_hijo(hijos, alelos)
            if Fitnes[fp] < 14:
                Matriz = Funciones.seleccion(Ganadores, hijos, Matriz, alelos, listaciudades)
            else:
                FitnesHijos = Funciones.valoracion(hijos, 2, alelos, listaciudades)
                Matriz = Funciones.selecciondirecta(Ganadores, hijos, Fitnes, FitnesHijos, Matriz)
            # __________________ OSKAR CHECK ----------------------
            for i in range(poblacion):
                if Fitnes[fp] > Fitnes[i]:
                    fp = i
            if secuencia == lim:
                res = int(raw_input('Detener ahora? si = 1 no = 2 '))
            if res is 1:
                B = False
            elif res is 2:
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
        Fitnes = (Funciones.valoracion(Matriz, poblacion, alelos, listaciudades))
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
        text = "Lapso de tiempo: %.10f segundos." % elapsed_time,
        self.mensajeLT.config(text="Lapso de tiempo: %.10f segundos." % elapsed_time)
        self.mensajeG.config(text=p)

        return 0


def main():
    Aplicacion()
    return 0


if __name__ == '__main__':
    main()
