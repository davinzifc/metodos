from conversoBaseBinaria import ConversorBaseBinaria as Binario
from conversoBaseDecimal import ConversorBaseDecimal as Decimal

class conversoIEEE64:
    def __init__(self):
        self.numDecimal = ""
        self.signo = ""
        self.exponente = ""
        self.coma = ""
        self.mantisa = ""
        pass

    def trasformDecimalTo64(self, numero = ""):
        decimal = Decimal(self.asingSigDes(numero))
        binario = decimal.decimalToBinarioEnteroFraccion(53)
        self.coma = binario.find(".") - 1
        temp = binario.split(".")
        self.mantisa = (temp[0][1:len(binario)]+temp[1])[0:52]
        temp = (self.coma)+1028
        self.exponente = decimal.decimalToBinarioEntero(str(temp))
        return self.signo+""+self.exponente+""+self.mantisa

    def trasformFrom64(self, form32 = "", pre = 20):
        self.signo = form32[0]
        self.exponente = form32[1:12]
        self.mantisa = form32[12:len(form32)]
        if len(self.mantisa) < 52:
            while len(self.mantisa) <=  52:
                self.mantisa = self.mantisa + "0"
        binario = Binario()
        self.coma = int(binario.binarioToDecimalEntero(self.exponente) - 1028)
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

obj = conversoIEEE64()
print(obj.trasformDecimalTo64("3789.1485"))
print(obj.trasformFrom64("0100000011111101100110100100110000001000001100010010011011101001"))