#importar la libreria flask
from flask import Flask, render_template, abort
#incializacion de la variable
app = Flask(__name__, template_folder= 'templates')
