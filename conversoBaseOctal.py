from Bases import Bases
from conversoBaseBinaria import ConversorBaseBinaria as Binario

class ConversorBaseOctal(Bases):
    def __init__(self, octal = ""):
        self.binario = Binario()
        self.listaOctal={'0':"000",'1':"001",'2':"010",'3':"011",'4':"100",'5':"101",'6':"110", '7':"111" }
        Bases.__init__(self, octal)
        pass

    def octalToBinario(self):
        binarioEntero = ""
        binarioFraccion = ""
        for oc in self.entero:
            binarioEntero = binarioEntero + self.listaOctal[oc]
        binarioEntero =binarioEntero[binarioEntero.find("1"):len(binarioEntero)]
        for oc in self.fraccion:
            binarioFraccion = binarioFraccion + self.listaOctal[oc]
        return  str(binarioEntero)+"."+str(binarioFraccion)

    def octalToDecimal(self):
        binario = self.octalToBinario().split(".")
        return self.binario.binarioToDecimalEnteroFraccion(0 ,binario[0], binario[1])

    def octalToHexa(self):
        binario = self.octalToBinario().split(".")
        return self.binario.binarioToHexaEnteroFraccion(binario[0], binario[1])

    pass     


## pruebas :D

obj = ConversorBaseOctal("26.0631464")

#Binario:       10110.00011001100110011010
#Octal:         26.0631464
#Hexadecimal:   16.1999A
#Decimal:       22.1000003814697265625
#obj.octalToDecimal()
#print("en decimal es: "+str(obj.octalToDecimal()))
#print("en binario es: "+str(obj.octalToBinario()))
#print("en hexadecimal es: "+str(obj.octalToHexa()))