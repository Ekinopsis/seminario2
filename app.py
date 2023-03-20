from flask import Flask
from flask import request
from flask import abort
from flask import redirect
from flask import url_for
from flask import render_template
from os import listdir
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/nosotros')
def nosotros():
    return render_template("nosotros.html")

@app.route('/producto')
def producto():
    return render_template("producto.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html"), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)
