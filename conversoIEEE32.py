from conversoBaseBinaria import ConversorBaseBinaria as Binario
from conversoBaseDecimal import ConversorBaseDecimal as Decimal

class conversoIEEE32:
    def __init__(self):
        self.numDecimal = ""
        self.signo = ""
        self.exponente = ""
        self.coma = ""
        self.mantisa = ""
        pass

    def trasformDecimalTo32(self, numero = ""):
        decimal = Decimal(self.asingSigDes(numero))
        binario = decimal.decimalToBinarioEnteroFraccion(24)
        self.coma = binario.find(".") - 1
        temp = binario.split(".")
        self.mantisa = (temp[0][1:len(binario)]+temp[1])[0:23]
        temp = (self.coma)+127
        self.exponente = decimal.decimalToBinarioEntero(str(temp))
        return self.signo+""+self.exponente+""+self.mantisa

    def trasformFrom32(self, form32 = "", pre = 20):
        self.signo = form32[0]
        self.exponente = form32[1:9]
        self.mantisa = form32[9:len(form32)]
        if len(self.mantisa) < 23:
            while len(self.mantisa) <=  23:
                self.mantisa = self.mantisa + "0"
        binario = Binario()
        self.coma = int(binario.binarioToDecimalEntero(self.exponente) - 127)
        self.mantisa = "1"+self.mantisa[0:self.coma]+"."+self.mantisa[self.coma:len(self.mantisa)]
        binario = Binario(self.mantisa)
        if self.signo == "0":
            return binario.binarioToDecimalEnteroFraccion(pre)
        if self.signo == "1":
            return "-"+str(binario.binarioToDecimalEnteroFraccion(pre))

    def asingSigDes(self, decimal = ""):
        if decimal[0] == "-":
            self.signo = "1"
            return decimal[1:len(decimal)]
        if decimal[0] != "-":
            self.signo = "0"
            return decimal

#obj = conversoIEEE32()
#print(obj.trasformDecimalTo32("1.1"))
#print(obj.trasformFrom32("0111111100011001100110011001100"))