from flask import Flask, render_template, request, redirect
app= Flask(__name__)

@app.route('/')
def index(red="0", green="0", blue="0"):
    return render_template("index.html")

@app.route('/colors', methods=['GET'])
def colors():
    print "Got GET Info"

    red= request.form['red']
    green= request.form['green']
    blue= request.form['blue']
    return render_template("index.html", red=red, green=green, blue=blue)

app.run(debug=True)