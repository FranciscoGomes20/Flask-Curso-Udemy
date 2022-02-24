from flask import render_template, request
from app import app, db
from app.models.tables import Pessoa

@app.route('/')
@app.route('/listagem')
def listagem():
    pessoas = Pessoa.query.all()
    return render_template('listagem.html', pessoas=pessoas, ordem='id')