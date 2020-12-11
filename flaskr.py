import sqlite3
from flask import Flask, render_template, request, g, redirect, url_for, \
    abort, session, flash

# Configurações

DATABASE = './tmp/flaskr.db'
USERNAME = 'admin'
PASSWORD = '123456'

# Criando o App
app = Flask(__name__)

def conectar_bd():
    return sqlite3.connect(DATABASE)

@app.before_request
def pre_requisicao():
    g.bd = conectar_bd()

@app.teardown_request
def pos_requisicao(exception):
    g.bd.close()

@app.route('/')
def exibir_entradas():
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cursor = g.bd.execute(sql)
    entradas = [dict(titulo=titulo, texto=texto) for titulo, texto in cursor.fetchall()]
    return render_template('exibir_entradas.html')