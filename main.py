import random
import tkinter as tk
from time import time
from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

from pip._vendor.distlib.compat import raw_input

import Funciones
import Grafica


class Aplicacion():
    def __init__(self):
        # <---------- VARIABLES ---------->
        self.isReady = False

        # <---------- UI ---------->
        self.ventana = Tk()
        self.ventana.geometry('600x320')
        self.ventana.configure(bg='beige')
        self.ventana.title('Problema del Agente Viajero')

        # <---------- TABS ---------->
        tab_control = ttk.Notebook(self.ventana)
        home = ttk.Frame(tab_control)
        tab_control.add(home, text="Home")
        tab_control.pack(expand=1, fill='both')

        # <---------- LABEL ---------->
        lblNumCiudades = Label(home, text="Numero de Ciudades", fg='black')
        lblNumIndividuos = Label(home, text="Numero de Individuos", fg='black')
        lblRepeticiones = Label(home, text="Repeticiones", fg='black')
        lblProbCruce = Label(home, text="Prob. de Cruce", fg='black')
        lblProbMut = Label(home, text="Prob. de Mutacion", fg='black')
        lblOrigen = Label(home, text="Origen", fg='black')

        # <---------- TEXTBOX ---------->
        self.txtNumCiudades = ttk.Entry(home, justify=tk.LEFT)
        self.txtNumIndividuos = ttk.Entry(home, justify=tk.LEFT)
        self.txtRepeticiones = ttk.Entry(home, justify=tk.LEFT)
        self.txtProbCruce = ttk.Entry(home, justify=tk.LEFT)
        self.txtProbMut = ttk.Entry(home, justify=tk.LEFT)
        self.txtOrigen = ttk.Entry(home, justify=tk.LEFT)

        # <---------- BUTTON ---------->
        self.btnPoblacion = ttk.Button(home, text="CREAR POBLACION", command=self.ciudades).place(x=100, y=250)
        self.btnIniciar = ttk.Button(home, text="INICIAR", command=self.algoritmo).place(x=250, y=250)
        self.btnSalir = ttk.Button(home, text="SALIR", command=self.ventana.destroy).place(x=350, y=250)

        # <---------- POSITION ---------->
        lblNumCiudades.place(x=10, y=5)
        self.txtNumCiudades.place(x=10, y=25)
        lblNumIndividuos.place(x=150, y=5)
        self.txtNumIndividuos.place(x=150, y=25)
        lblRepeticiones.place(x=290, y=5)
        self.txtRepeticiones.place(x=290, y=25)
        lblProbCruce.place(x=430, y=5)
        self.txtProbCruce.place(x=430, y=25)
        lblProbMut.place(x=10, y=50)
        self.txtProbMut.place(x=10, y=70)
        lblOrigen.place(x=150, y=50)
        self.txtOrigen.place(x=150, y=70)

        # <---------- RESULTS ---------->
        self.lblTiempo = Label(home, text="", fg='black').place(x=10, y=150)
        self.lblGanador = Label(home, text="", fg='black').place(x=10, y=190)

        # <---------- INITIAL DATA ---------->
        self.txtNumCiudades.insert(0, "test")
        self.txtNumIndividuos.insert(0, 1000)
        self.txtRepeticiones.insert(0, 10000)
        self.txtProbCruce.insert(0, 0.85)
        self.txtProbMut.insert(0, 0.01)
        self.txtOrigen.insert(0, 0)
        self.txtProbCruce.config(state=tk.DISABLED)
        self.txtProbMut.config(state=tk.DISABLED)
        self.ventana.mainloop()

    def algoritmo(self):
        if self.isReady:
            _individuos = int(self.txtNumIndividuos.get())
            _origen = int(self.txtOrigen.get())
            _ciudades = self.ciudades
            _repeticiones = int(self.txtRepeticiones.get())
            _mejorGrafica = [-1]
            _ciudadesText = self.txtNumCiudades.get()

            print("Iniciando Algoritmo...")
            start_time = time()

            Poblacion = []

            for i in range(_individuos):
                Poblacion.append(Funciones.individuo(_ciudades, _origen))

            for ind in range(_individuos):
                print("Individuo ", (ind+1), ": ", Poblacion[ind])

            Fitness = Funciones.evaluar(Poblacion, len(Poblacion), _ciudades, self.listaCiudades)

            isContinue = True
            secuencia = 1
            limite = _repeticiones
            res = 'x'

            while isContinue:
                print("Repeticion ", secuencia)

                PosPadres = Funciones.torneo(_individuos, Fitness)
                print("Posiciones padres: ", PosPadres)

                _probCruce = float(self.txtProbCruce.get())
                _probMut = float(self.txtProbMut.get())
                Hijos = []

                if round(random.random(), 3) <= _probCruce:
                    Hijos = Funciones.cruce(Poblacion, PosPadres, _ciudades)
                else:
                    for i in range(2):
                        Hijos.append(Poblacion[PosPadres[i]])

                if round(random.random(), 3) <= _probMut:
                    Funciones.mutacion(Hijos, _ciudades)
                    print("MUTACION AQUI")

                FitnessHijos = Funciones.evaluar(Hijos, len(Hijos), _ciudades, self.listaCiudades)

                Mejores = Funciones.seleccionDirecta(Poblacion, PosPadres, Fitness, Hijos, FitnessHijos)
                Funciones.remplazo(Poblacion, PosPadres, Fitness, Mejores)
                # TODO: Mejor de todos

                if secuencia >= limite:
                    res = int(raw_input("Desea continuar? si = 1"))
                if res is 1:
                    limite += _repeticiones
                    res = 'x'
                elif res is not 'x':
                    isContinue = False

                _mejor = Funciones.mejor(Poblacion, Fitness)

                if _ciudadesText == 'test':
                    if _mejor[0] is 14:
                        isContinue = False

                if _mejorGrafica[0] is not _mejor[0]:
                    _mejorGrafica = _mejor
                    Grafica.grafica(1, _mejorGrafica[1], _mejorGrafica[0], secuencia, self.listaCiudades, (_ciudades+1), 15)

                secuencia += 1

            print("<--TERMINADO-->")

            for i in range(_individuos):
                print("Fitness ", i, ": ", Fitness[i], " --> Individuo: ", Poblacion[i])

            _mejor = Funciones.mejor(Poblacion, Fitness)
            print("Individuo ", _mejor[2], ": ", _mejor[1])
            print("Fitness: ", _mejor[0])

            elapsed_time = time() - start_time
            print(elapsed_time)
        else:
            print("Necesito Ciudades :(")

    def ciudades(self):
        if not self.isReady:
            print("Creando Ciudades...")

            self.listaCiudades = []
            _ciudades = self.txtNumCiudades.get()

            if _ciudades == "test":
                self.ciudades = 14
                self.txtOrigen.delete(0)
                self.txtOrigen.insert(0, 0)
                self.txtOrigen.config(state=DISABLED)
                self.listaCiudades = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1],
                                      [5, 2], [4, 2], [3, 2], [2, 2], [1, 2], [0, 2], [0, 1],
                                      [0, 0]]
            else:
                self.ciudades = int(_ciudades)
                self.listaCiudades = Funciones.crearCiudades(self.ciudades)

            self.isReady = True
            print("Ciudades Creadas :D")
            print(self.listaCiudades)
            Grafica.grafica(ciudades=self.listaCiudades, numCiudades=self.ciudades)
        else:
            print("Ya tengo ciudades :)")


def main():
    Aplicacion()
    return 0


if __name__ == '__main__':
    main()
