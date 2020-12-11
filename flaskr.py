import sqlite3
from flask import Flask, render_template, request, g, redirect, url_for, \
    abort, session, flash

# Configurações


DATABASE = './tmp/flaskr.db'
USERNAME = 'admin'
PASSWORD = '123456'

# Criando o APP
app = Flask(__name__)

def conectar_bd():
    return sqlite3.connect(DATABASE)
