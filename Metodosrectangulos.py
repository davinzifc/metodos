from sympy import sin, cos, tan, cot, exp, ln, re, pi
import numpy as np
import matplotlib.pyplot as plt
from sympy.functions import sign
from sympy import sympify

#############################################################
#   @author: Davinzi
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
class MetodoReactangulos:

    def __init__(self, xi, xf, cantidad, f):
        self.xi = float(sympify(xi))
        self.xf = float(sympify(xf))
        self.cantidad = int(cantidad)
        self.Fs = str(f).replace("**", "^").replace("*", "")
        self.f = lambda x: eval(f)
        self.b = (self.xf - self.xi) / self.cantidad
        pass

    def izquierdo(self):
        sumatoria = 0
        for h in range(self.cantidad):
            if isinstance(self.f(self.xi+(h)*self.b), float) or (self.f(self.xi+(h)*self.b)).is_real:
                sumatoria += (self.f(self.xi+(h)*self.b))
            else:
                sumatoria += 0
        return float(self.b * sumatoria)
        

    def derecho(self):
        sumatoria = 0
        for h in range(self.cantidad):
            if isinstance(self.f(self.xi+(h+1)*self.b), float) or (self.f(self.xi+(h+1)*self.b)).is_real:
                sumatoria += (self.f(self.xi+(h+1)*self.b))
            else:
                sumatoria += 0
        return float(self.b * sumatoria)
        

    def central(self):
        sumatoria = 0
        for h in range(self.cantidad):
            if isinstance((self.f((self.xi+(h+1)*self.b + self.xi+(h)*self.b) / 2)), float) or (self.f((self.xi+(h+1)*self.b + self.xi+(h)*self.b) / 2)).is_real:
                sumatoria += (self.f((self.xi+(h+1)*self.b + self.xi+(h)*self.b) / 2))
            else:
                sumatoria += 0
        return float(self.b * sumatoria)

#############################################################
#   graficar(r, pu)        
#
#   r:..........mostrar rectangulos [False] por defecto
#   pu:.........puntos de los rectangulos por defecto [1]
#               0: izquierdo
#               1: medio
#               2: derecho
#############################################################
    def graficar(self, r = False, pu = 1):
        if abs(self.xi) > abs(self.xf):
            p = np.linspace(-abs(self.xi + 1),abs(self.xi + 1),100)
        else:
            p = np.linspace(-abs(self.xf + 1),abs(self.xf + 1),100)
        var = []
        for v in p:
            var.append(float(self.f(v)))
        plt.plot(p,var)
        plt.fill_between(p, var, 0 , where=(p>=self.xi ) & (p<=self.xf ), color='blue', alpha=.25)  
        plt.xlabel('x')
        plt.ylabel('f(x) = '+str(self.Fs))
        bx = []
        by = []
        for h in range(self.cantidad):
            bx.append((self.xi+(h+1)*self.b + self.xi+(h)*self.b) / 2)
            if pu == 0:
                by.append(re(self.f(self.xi+(h)*self.b)))    
            if pu == 2:
                by.append(re(self.f(self.xi+(h+1)*self.b)))
            if pu == 1:
                by.append(re(self.f((self.xi+(h+1)*self.b + self.xi+(h)*self.b) / 2)))
        if r == True:
            plt.bar(bx,by,width=self.b,alpha=0.5,facecolor='orange', edgecolor = "k")
        plt.title('Suma de Riemann para f(x)')
        plt.grid()
        plt.show()
        pass
        

    def getXi(self):
        return self.xi
        

    def getXf(self):
        return self.xf
        

    def getCantidad(self):
        return self.cantidad
        

    def getF(self):
        return self.f
        

    def getB(self):
        return self.b


    def setXi(self, xi):
        self.xi = xi
        pass
        

    def setXf(self, xf):
        self.xf = xf
        pass
        

    def setCantidad(self, cantidad):
        self.cantidad = cantidad
        pass
        

    def setF(self, f):
        self.f = f
        pass
        

    def setB(self, b):
        self.b = b
        pass

    pass
