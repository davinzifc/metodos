from Bases import Bases
from conversoBaseBinaria import ConversorBaseBinaria as Binario

class ConversorBaseDecimal(Bases):
    def __init__(self, decimal = ""):
        self.binario = Binario()
        Bases.__init__(self, decimal)
        pass

    def decimalToBinarioEntero(self, entero = ""):
        if entero == "":
            entero = self.entero
        numero=int(entero)
        numerobinario=""
        if numero == 0.0:
           numerobinario=numerobinario+""+str(0)
        while numero>0.0:
            if numero%2==0:
                numerobinario=numerobinario+""+str(0)
                numero=numero/2    
            if numero%2==1:
                numerobinario=numerobinario+""+str(1)
                numero=(numero-1)/2
        numerobinario=numerobinario[::-1]
        return str(numerobinario)

    def decimalToBinarioFraccion(self, fraccion = "", presicion = 20):
        if fraccion == "":
            fraccion = self.fraccion
        numero=float("0."+str(fraccion))
        resultado=""
        i=0
        while i<presicion:
            numero=numero*2
            if numero>=1.0:
                numero=numero-1.0
                resultado+="1"
            else:
                resultado+="0"
            i+=1
        return str(resultado)

    def decimalToBinarioEnteroFraccion(self, presicion = 20, entero = "", fraccion = ""):
        if entero == "":
            entero = self.entero
        if fraccion == "":
            fraccion = self.fraccion
        return self.decimalToBinarioEntero(entero)+"."+self.decimalToBinarioFraccion(fraccion, presicion)

    def decimalToOctal(self):
        binario = self.decimalToBinarioEnteroFraccion().split(".")
        return self.binario.binarioToOctalEnteroFraccion(binario[0], binario[1])
    
    def decimalToHexa(self):
        binario = self.decimalToBinarioEnteroFraccion().split(".")
        return self.binario.binarioToHexaEnteroFraccion(binario[0], binario[1])
    
    pass

## pruebas :D

#obj = ConversorBaseDecimal("22.1000003814697265625")

#Binario:       10110.00011001100110011010
#Octal:         26.0631464
#Hexadecimal:   16.1999A
#Decimal:       22.1000003814697265625

#print("en binario es: "+str(obj.decimalToBinarioEnteroFraccion()))
#print("en octal es: "+str(obj.decimalToOctal()))
#print("en hexadecimal es: "+str(obj.decimalToHexa()))
