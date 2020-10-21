from flask import Flask, render_template, request, redirect, url_for, jsonify
from simpson13 import Simpson13
from simpson38 import Simpson38
from MetodoMontecarlo import MetodoMontercarlo
from Metodosrectangulos import MetodoReactangulos
from MetodoTrapecio import MetodoTrapecio
import numpy as np

app = Flask(__name__)
simp13 = [""]*5
simp13[4] = False
simp38 = [""]*5
simp38[4] = False
monte = [""]*4
rect = [""]*4
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
