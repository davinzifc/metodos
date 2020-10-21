from sympy import sin, cos, tan, cot, exp, ln, re, pi, Symbol, diff
import numpy as np
import matplotlib.pyplot as plt
from sympy.functions import sign
from sympy import sympify
import random

class Simpson38:
    def __init__(self, xi, xf, cantidad, f, ab = False):
        self.xi = float(sympify(xi))
        self.xf = float(sympify(xf))
        self.cantidad = self.cantidadMod(int(cantidad))
        self.Fs = str(f).replace("**", "^").replace("*", "")
        self.f = lambda x: eval(f)
        self.h = (self.xf - self.xi) / self.cantidad
        self.x = Symbol('x')
        self.fd4 = lambda x: eval(str(diff(str(f), self.x, 4)))
        self.ab = ab
        pass

    def fy(self):
        xin = []
        xfn = []
        for i in range(self.cantidad + 1):
            xin.append(self.xi+(i*self.h))
        for i in xin:
            if isinstance(self.f(i), float) or (self.f(i)).is_real:
                if self.ab:
                    xfn.append(abs(self.f(i)))
                else:
                    xfn.append(self.f(i))
            else:
                xfn.append(0)
        return xin, xfn

    def calculo38(self):
        data = self.fy()
        sum2 = 0
        sum3 = 0
        for i in data[1][1:-1:3]:
            sum2 += data[1][data[1].index(i)] + data[1][data[1].index(i)+1]
        for i in data[1][3:-1:3]:
            sum3 += i 
        return float((3*self.h)/8*(data[1][0] + data[1][-1] + 3*sum2 + 2*sum3))

    def cantidadMod(self, cantidad):
        if (cantidad %  3) == 1:
            return int(cantidad + 2)
        elif (cantidad %  3) == 2:
            return int(cantidad + 1)
        return int(cantidad)

    def error(self):
        return float((-3*self.h**5/80)*self.fd4(random.randint(int(self.xi), int(self.xf))))