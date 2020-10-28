from Bases import Bases

class ConversorBaseBinaria(Bases):
    def __init__(self, binario=""):
        Bases.__init__(self, binario)
        pass

    def binarioToDecimalEntero(self, entero):
        cant=len(entero)
        numi=0
        num1=entero[::-1]
        for i in range(cant):
            numi=numi+(int(num1[0+i:i+1])*(2**i))
            numi=int(numi)
        return float(numi)

    def binarioToDecimalFraccion(self, fraccion , redondeo = 20):
        numi=0
        num2 = fraccion
        cant=len(num2)
        for i in range(cant):
             numi=numi+(int(num2[0+i:i+1])*(1/(2**(i+1))))
             numi=float(numi)
        return round(float(numi), redondeo)

    def binarioToDecimalEnteroFraccion(self, redondeo = 20 ,entero = "", fraccion = ""):
        if entero == "":
            entero = self.entero
        if fraccion == "":
            fraccion = self.fraccion
        if redondeo  == 0:
            redondeo  = 20  
        return round(float(self.binarioToDecimalEntero(entero)) + float(self.binarioToDecimalFraccion(fraccion)), int(redondeo))

    def binarioToOctalEnteo(self, entero):
        octal = ""
        binario = str(entero)
        length = len(binario)
        if (length % 3) == 1:
            binario = "00"+binario
        if (length % 3) == 2:
            binario = "0"+binario
        for x in range(int(len(binario)/3)):
            octal = octal + str(int(self.binarioToDecimalEntero(binario[x*3:(x+1)*3])))
        return str(octal)

    def binarioToOctalFraccion(self, fraccion):
        octal = ""
        binario = str(fraccion)
        length = len(binario)
        if (length % 3) == 1:
            binario = binario+"00"
        if (length % 3) == 2:
            binario = binario+"0"
        for x in range(int(len(binario)/3)):
            octal = octal + str(int(self.binarioToDecimalEntero(binario[x*3:(x+1)*3])))
        return str(octal)

    def binarioToOctalEnteroFraccion(self, entero = "", fraccion = ""):
        if entero == "":
            entero = self.entero
        if fraccion == "":
            fraccion = self.fraccion
        return self.binarioToOctalEnteo(entero)+"."+self.binarioToOctalFraccion(fraccion)

    def binarioToHexaEntero(self, entero):
        hexa = ""
        binario = str(entero)
        length = len(binario)
        if (length % 4) == 1:
            binario = "000"+binario
        if (length % 4) == 2:
            binario = "00"+binario
        if (length % 4) == 3:
            binario = "0"+binario
        for x in range(int(len(binario)/4)):
            number = int(self.binarioToDecimalEntero(binario[x*4:(x+1)*4]))
            if number < 10:
                hexa = hexa + str(number)
            if number > 9:
                hexa = hexa + self.listaHexa[number]
        return str(hexa)

    def binarioToHexaFraccion(self, fraccion):
        hexa = ""
        binario = str(fraccion)
        length = len(binario)
        if (length % 4) == 1:
            binario = binario+"000"
        if (length % 4) == 2:
            binario = binario+"00"
        if (length % 4) == 3:
            binario = binario+"0"
        for x in range(int(len(binario)/4)):
            number = int(self.binarioToDecimalEntero(binario[x*4:(x+1)*4]))
            if number < 10:
                hexa = hexa + str(number)
            if number > 9:
                hexa = hexa + self.listaHexa[number]
        return str(hexa)
    
    def binarioToHexaEnteroFraccion(self, entero = "", fraccion = ""):
        if entero == "":
            entero = self.entero
        if fraccion == "":
            fraccion = self.fraccion
        return self.binarioToHexaEntero(entero)+"."+self.binarioToHexaFraccion(fraccion)


## pruebas :D

# obj = ConversorBaseBinaria("10110.00011001100110011010")

#Binario:       10110.00011001100110011010
#Octal:         26.0631464
#Hexadecimal:   16.1999A
#Decimal:       22.1000003814697265625

#print("en decimal es: "+str(obj.binarioToDecimalEnteroFraccion()))
#print("en octal es: "+str(obj.binarioToOctalEnteroFraccion()))
#print("en hexadecimal es: "+str(obj.binarioToHexaEnteroFraccion()))


