from sympy import sin, cos, tan, cot, exp, ln, re, pi, Symbol, diff
import numpy as np
import matplotlib.pyplot as plt
from sympy.functions import sign
from sympy import sympify
import random

class Simpson13:
    def __init__(self, xi, xf, cantidad, f, ab = False):
        self.xi = float(sympify(xi))
        self.xf = float(sympify(xf))
        self.cantidad = int(cantidad) if (int(cantidad) %  2) == 0 else int(cantidad) + 1
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

    def calculo13(self):
        data = self.fy()
        sum2 = 0
        sum3 = 0
        for i in data[1][1::2]:
            sum2 += i
        for i in data[1][2:-2:2]:
            sum3 += i
        return float(self.h/3*(data[1][0]+4*(sum2)+2*(sum3)+data[1][-1]) )

    def error(self):
        return float((-self.h**5/90)*self.fd4(random.randint(int(self.xi), int(self.xf))))