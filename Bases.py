class Bases:
    
    def __init__(self, numero = ""):
        self.listaHexa = {10:"A", 11:"B",12:"C",13:"D",14:"E", 15:"F"}
        self.listaHexaCom = {'0':"0000",'1':"0001",'2':"0010",'3':"0011",'4':"0100",'5':"0101",'6':"0110", '7':"0111",'8':"1000",'9':"1001",'A':"1010",'B':"1011",'C':"1100",'D':"1101",'E':"1110",'F':"1111"}
        self.entero = ""
        self.fraccion = ""
        self.separarEnteroFraccion(numero)
        pass

    def separarEnteroFraccion(self,valorAlfanumerico):
        separar = valorAlfanumerico.split(".")
        if len(separar) > 1:
            self.entero = separar[0]
            self.fraccion = separar[1]
        else:
            self.entero = separar[0]
            self.fraccion = "0"
        pass
    
    #       get & set       #

    def getEntero(self):
        return self.entero
    
    def setEntero(self,nume):
        self.entero=nume
        pass

    def getFraccion(self):
        return self.fraccion
    
    def setFraccion(self,num):
        self.fraccion=num
        pass

