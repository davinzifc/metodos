from Bases import Bases
from conversoBaseBinaria import ConversorBaseBinaria as Binario

class ConversorBaseHexadecimal(Bases):
    def __init__(self, hexadecimal=""):
        self.binario = Binario()
        Bases.__init__(self, hexadecimal)
        pass

    def hexadecimalToBinario(self):
        binarioEntero = ""
        binarioFraccion = ""
        for oc in self.entero:
            binarioEntero = binarioEntero + self.listaHexaCom[oc]
        binarioEntero =binarioEntero[binarioEntero.find("1"):len(binarioEntero)]
        for oc in self.fraccion:
            binarioFraccion = binarioFraccion + self.listaHexaCom[oc]
        return  str(binarioEntero)+"."+str(binarioFraccion)

    def hexadecimalToDecimal(self):
        binario = self.hexadecimalToBinario().split(".")
        return self.binario.binarioToDecimalEnteroFraccion(0, binario[0], binario[1])
    
    def hexadecimalToOctal(self):
        binario = self.hexadecimalToBinario().split(".")
        return self.binario.binarioToOctalEnteroFraccion(binario[0], binario[1])


## pruebas :D

#obj = ConversorBaseHexadecimal('16.1999A')

#Binario:       10110.00011001100110011010
#Octal:         26.0631464
#Hexadecimal:   16.1999A
#Decimal:       22.1000003814697265625

#print("en decimal es: "+str(obj.hexadecimalToDecimal()))
#print("en binario es: "+str(obj.hexadecimalToBinario()))
#print("en octal es: "+str(obj.hexadecimalToOctal()))
