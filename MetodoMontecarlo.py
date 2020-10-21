from sympy import sin, cos, tan, cot, exp, ln, re, pi, Symbol, diff
import numpy as np
import matplotlib.pyplot as plt
from sympy.functions import sign
from sympy import sympify
import random

class MetodoMontercarlo:

    def __init__(self, xi, xf, cantidad, f):
        self.xi = float(sympify(xi))
        self.xf = float(sympify(xf))
        self.cantidad = int(cantidad)
        self.Fs = str(f).replace("**", "^").replace("*", "")
        self.f = lambda x: eval(f)
        pass

    def cotaSup(self):
        dx = (self.xf - self.xi)/1000
        mayor = float(self.f(self.xi))
        for v in range(1000):
            if mayor < float(self.f(self.xi+(v*dx))):
                mayor = float(self.f(self.xi+(v*dx)))
        print(mayor)
        return mayor
    
    def calcMonte(self):
        cota = self.cotaSup()
        ex = 0
        for v in range(self.cantidad):
            xi = self.xi + random.random() * (self.xf - self.xi)
            yi = random.random() * cota
            
            if yi <= float(self.f(xi)):
                ex += 1
        return (ex / self.cantidad) * (float(self.xf) - float(self.xi)) * cota