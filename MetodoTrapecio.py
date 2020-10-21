from sympy import sin, cos, tan, cot, exp, ln, re
import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify

#############################################################
#   @authors: AlfiieGonzalez, Davinzi
#   v. 0.0.2
#############################################################
#   MetodoReactangulos(xi, xf, cantidad, f)
#
#   xi:.........punto inicial
#   xf:.........punto final
#   cantidad:...cantidad de cuadrados a calcular
#   f:..........funcion
#############################################################
#   Fs:.........Formula a mostrar en la tabla (Alpha)
#   b:..........base
#############################################################

class MetodoTrapecio:

    def __init__(self, xi, xf, cantidad, f):
        self.xi = float(sympify(xi))
        self.xf = float(sympify(xf))
        self.cantidad = int(cantidad)
        self.Fs = str(f).replace("**", "^").replace("*", "")
        self.f = lambda x: eval(f)
        self.b = (self.xf - self.xi) / self.cantidad
        self.muestras = self.cantidad + 1
        self.muestrasLinea = self.muestras * 10
        pass

    def trapecios(self):
        xi = self.xi
        suma = 0
        for i in range(0,self.cantidad,1):
            if isinstance((self.b*(self.f(xi) + self.f(xi + self.b)) / 2), float) or (self.b*(self.f(xi) + self.f(xi + self.b)) / 2).is_real:
                atrapecio = (self.b*(self.f(xi) + self.f(xi + self.b)) / 2)
 
            else:
                atrapecio = 0
            suma = suma+atrapecio
            xi = xi+self.b
        integral = suma
        return float(integral)

    def defPuntoLinea(self):
        xi= np.linspace(self.xi,self.xf,self.muestras)
        xk= np.linspace(self.xi,self.xf,self.muestrasLinea)
        fi = []
        fk = []
        for v in xi:
            fi.append(re(self.f(v)))
        for v in xk:
            fk.append(re(self.f(v)))
        return  fi, fk

    def graficar(self):
        xi= np.linspace(self.xi,self.xf,self.muestras)
        xk= np.linspace(self.xi,self.xf,self.muestrasLinea)
        datos = self.defPuntoLinea()
        plt.plot(xi,datos[0],'ro')
        plt.plot(xk,datos[1], color='g')
        covMat = np.array(datos[0], dtype=float)
        plt.fill_between(xi, 0, covMat, color='b')
        for i in range (0,self.muestras,1):
            plt.axvline(xi[i], color='y')
        plt.show()

    pass
