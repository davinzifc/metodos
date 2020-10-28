from flask import Flask, render_template, request, redirect, url_for, jsonify
from simpson13 import Simpson13
from simpson38 import Simpson38
from MetodoMontecarlo import MetodoMontercarlo
from Metodosrectangulos import MetodoReactangulos
from MetodoTrapecio import MetodoTrapecio
import numpy as np
from conversoBaseBinaria import ConversorBaseBinaria as Binario
from conversoBaseDecimal import ConversorBaseDecimal as Decimal
from conversoBaseHexadecimal import ConversorBaseHexadecimal as Hexadecimal
from conversoBaseOctal import ConversorBaseOctal as Octal
from conversoIEEE32 import conversoIEEE32 as bits32
from conversoIEEE64 import conversoIEEE64 as bits64
import re

app = Flask(__name__)
simp13 = [""]*5
simp13[4] = False
simp38 = [""]*5
simp38[4] = False
monte = [""]*4
rect = [""]*4
bass1 = [""]*2
# Creating simple Routes 
@app.route('/test')
def test():
    return render_template("layout.html")

@app.route('/montecarlo')
def montecarlo():
    if not monte or monte[0] == "" or monte[1] == "" or monte[2] == "" or monte[3] == "":
       area1 = ""
       monte1 = [""] * 4 
    else:
        obj= MetodoMontercarlo(monte[1], monte[2], monte[3], monte[0])
        area1 = obj.calcMonte()
        monte1 = monte
    return render_template("montecarlo.html", area = area1, datos = monte1 )

@app.route('/rectangulos')
def rectangulos():
    if not rect or rect[0] == "" or rect[1] == "" or rect[2] == "" or rect[3] == "":
       area1 = [""] * 4
       rect1 = [""] * 4 
    else:
        obj = MetodoReactangulos(rect[1], rect[2], rect[3], rect[0])
        obj2 = MetodoTrapecio(rect[1], rect[2], rect[3], rect[0])
        area1 = [obj.izquierdo(), obj.central(), obj.derecho(), obj2.trapecios()]
        rect1 = rect
    return render_template("rectangulos.html", area = area1, datos = rect1 )

@app.route('/bases')
def bases():
    global bass1
    datos1 = [""]*6
    if not bass1 or bass1[1] == "":
        bass1 = [""] * 2
    else:
        if(bass1[0] == "Base 2"):
            if re.match("^[0-1.]*$", bass1[1]):
                obj = Binario(bass1[1])
                datos1[0] = bass1[1]
                datos1[1] = obj.binarioToOctalEnteroFraccion()
                datos1[2] = obj.binarioToDecimalEnteroFraccion()
                datos1[3] = obj.binarioToHexaEnteroFraccion()
                obj1 = bits32()
                obj2 = bits64()
                datos1[4] = obj1.trasformDecimalTo32(str(datos1[2]))
                datos1[5] = obj2.trasformDecimalTo64(str(datos1[2]))
            else:
                print(bass1[1]+" mas de 1 o contiene letras")
        if(bass1[0] == "Base 8"):
            if re.match("^[0-7.]*$", bass1[1]):
                obj = Octal(bass1[1])
                datos1[0] = obj.octalToBinario()
                datos1[1] = bass1[1]
                datos1[2] = obj.octalToDecimal()
                datos1[3] = obj.octalToHexa()
                obj1 = bits32()
                obj2 = bits64()
                datos1[4] = obj1.trasformDecimalTo32(str(datos1[2]))
                datos1[5] = obj2.trasformDecimalTo64(str(datos1[2]))
            else:
                print(bass1[1]+" mas de 7 o contiene letras")
        if(bass1[0] == "Base 10"):
            if re.match("^[0-9.]*$", bass1[1]):
                obj = Decimal(bass1[1])
                datos1[0] = obj.decimalToBinarioEnteroFraccion()
                datos1[1] = obj.decimalToOctal()
                datos1[2] = bass1[1]
                datos1[3] = obj.decimalToHexa()
                obj1 = bits32()
                obj2 = bits64()
                datos1[4] = obj1.trasformDecimalTo32(str(datos1[2]))
                datos1[5] = obj2.trasformDecimalTo64(str(datos1[2]))
            else:
                print(bass1[1]+" contiene letras")
        if(bass1[0] == "Base 16"):
            bass1[1] = bass1[1].upper()
            if re.match("^[0-9A-F.]*$", bass1[1]):
                obj = Hexadecimal(bass1[1])
                datos1[0] = obj.hexadecimalToBinario()
                datos1[1] = obj.hexadecimalToOctal()
                datos1[2] = obj.hexadecimalToDecimal()
                datos1[3] = bass1[1]
                obj1 = bits32()
                obj2 = bits64()
                datos1[4] = obj1.trasformDecimalTo32(str(datos1[2]))
                datos1[5] = obj2.trasformDecimalTo64(str(datos1[2]))
            else:
                print(bass1[1]+" contiene letras no aceptadas")
        if(bass1[0] == "IEEE 32"):
            bass1[1] = bass1[1].upper()
            if re.match("^[0-1.]*$", bass1[1]) and len(bass1[1]) <= 32:
                obj = bits32()
                datos1[2] = obj.trasformFrom32(bass1[1])
                obj4 = Decimal(str(datos1[2]))
                datos1[0] = obj4.decimalToBinarioEnteroFraccion()
                datos1[1] = obj4.decimalToOctal()
                datos1[3] = obj4.decimalToHexa()
                obj2 = bits64()
                datos1[4] = bass1[1]
                datos1[5] = obj2.trasformDecimalTo64(str(datos1[2]))
            else:
                print(bass1[1]+" es mayor a 1 tiene mas de 32 caracteres")
        if(bass1[0] == "IEEE 64"):
            bass1[1] = bass1[1].upper()
            if re.match("^[0-1.]*$", bass1[1]) and len(bass1[1]) <= 64:
                obj = bits64()
                datos1[2] = obj.trasformFrom64(bass1[1])
                obj4 = Decimal(str(datos1[2]))
                datos1[0] = obj4.decimalToBinarioEnteroFraccion()
                datos1[1] = obj4.decimalToOctal()
                datos1[3] = obj4.decimalToHexa()
                obj2 = bits32()
                datos1[4] = obj2.trasformDecimalTo32(str(datos1[2]))
                datos1[5] = bass1[1]
            else:
                print(bass1[1]+" es mayor a 1 tiene mas de 64 caracteres")
    return render_template("bases.html", datos = datos1)


@app.route('/simpson13')
def simpson13():
    if not simp13 or simp13[0] == "" or simp13[1] == "" or simp13[2] == "" or simp13[3] == "":
       area1 = ""
       error1 = "" 
       simp131 = [""] * 4 
    else:
        obj= Simpson13(simp13[1], simp13[2], simp13[3], simp13[0], simp13[4])
        area1 = obj.calculo13()
        error1 = obj.error()
        simp131 = simp13
    return render_template("simpson13.html", area = area1, error = error1, datos = simp131 )
    
@app.route('/simpson38')
def simpson38():
    if not simp38 or simp38[0] == "" or simp38[1] == "" or simp38[2] == "" or simp38[3] == "":
       area1 = ""
       error1 = "" 
       simp381 = [""] * 4 
    else:
        obj= Simpson38(simp38[1], simp38[2], simp38[3], simp38[0], simp38[4])
        area1 = obj.calculo38()
        error1 = obj.error()
        simp381 = simp38
    return render_template("simpson38.html", area = area1, error = error1, datos = simp381 )

@app.route('/calc13', methods = ['POST'])
def calc13():
    if request.method == 'POST':
        simp13[0] = request.form['function']
        simp13[1] = request.form['extremea']
        simp13[2] = request.form['extremeb']
        simp13[3] = request.form['partitions']
        try:
            request.form['absolute']
            simp13[4] = True
        except:
            simp13[4] = False
    return redirect(url_for('simpson13'))

@app.route('/calc38', methods = ['POST'])
def calc38():
    if request.method == 'POST':
        simp38[0] = request.form['function']
        simp38[1] = request.form['extremea']
        simp38[2] = request.form['extremeb']
        simp38[3] = request.form['partitions']
        try:
            request.form['absolute']
            simp38[4] = True
        except:
            simp38[4] = False
    return redirect(url_for('simpson38'))

@app.route('/calcBass', methods = ['POST'])
def calcBass():
    if request.method == 'POST':
        bass1[0] = request.form['bass']
        bass1[1] = request.form['value']
        print(bass1[0])
    return redirect(url_for('bases'))

@app.route('/calcMonte', methods = ['POST'])
def calcMonte():
    if request.method == 'POST':
        monte[0] = request.form['function']
        monte[1] = request.form['extremea']
        monte[2] = request.form['extremeb']
        monte[3] = request.form['points']
    return redirect(url_for('montecarlo'))

@app.route('/calcRect', methods = ['POST'])
def calcRect():
    if request.method == 'POST':
        rect[0] = request.form['function']
        rect[1] = request.form['extremea']
        rect[2] = request.form['extremeb']
        rect[3] = request.form['partitions']
    return redirect(url_for('rectangulos'))    


@app.route('/test/about/')
def about_test():
    return render_template("layout.html")

# Routes to Render Something
@app.route('/')
def home():
    return render_template("about.html")

@app.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)
