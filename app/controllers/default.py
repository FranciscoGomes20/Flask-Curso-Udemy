from crypt import methods
from flask import render_template, request
from app import app, db
from app.models.tables import Pessoa

@app.route('/')
@app.route('/listagem')
def listagem():
    pessoas = Pessoa.query.all()
    return render_template('listagem.html', pessoas=pessoas, ordem='id')

@app.route('/selecao/<int:id>')
def selecao(id=0):
    pessoas = Pessoa.query.filter_by(id=id).all()
    return render_template('listagem.html', pessoas=pessoas, ordem='id')

@app.route('/ordenacao/<campo>/<ordem_anterior>')
def ordenacao(campo='id', ordem_anterior=''):
    if campo  == 'id':
        if ordem_anterior == campo:
            pessoas = Pessoa.query.order_by(Pessoa.id.desc()).all()
        else:
            pessoas = Pessoa.query.order_by(Pessoa.id).all()
    elif campo == 'nome':
        if ordem_anterior == campo:
            pessoas = Pessoa.query.order_by(Pessoa.nome.desc()).all()
        else:
            pessoas = Pessoa.query.order_by(Pessoa.nome).all()
    elif campo == 'idade':
        if ordem_anterior == campo:
            pessoas = Pessoa.query.order_by(Pessoa.idade.desc()).all()
        else:
            pessoas = Pessoa.query.order_by(Pessoa.idade).all()
    elif campo == 'sexo':
        if ordem_anterior == campo:
            pessoas = Pessoa.query.order_by(Pessoa.sexo.desc()).all()
        else:
            pessoas = Pessoa.query.order_by(Pessoa.sexo).all()
    elif campo == 'salario':
        if ordem_anterior == campo:
            pessoas = Pessoa.query.order_by(Pessoa.salario.desc()).all()
        else:
            pessoas = Pessoa.query.order_by(Pessoa.salario).all()
    else:
        pessoas = Pessoa.query.order_by(Pessoa.id).all()
    return render_template('listagem.html', pessoas=pessoas, ordem=campo)

@app.route('/consulta', methods=['POST'])
def consulta():
    consulta = '%'+request.form.get('consulta')+'%'
    campo = request.form.get('campo')

    if campo == 'nome':
        pessoas = Pessoa.query.filter(Pessoa.nome.like(consulta)).all()
    elif campo == 'idade':
        pessoas = Pessoa.query.filter(Pessoa.idade.like(consulta)).all()
    elif campo == 'sexo':
        pessoas = Pessoa.query.filter(Pessoa.sexo.like(consulta)).all()
    elif campo == 'salario':
        pessoas = Pessoa.query.filter(Pessoa.salario.like(consulta)).all()
    else:
        pessoas = Pessoa.query.all()
    return render_template('listagem.html', pessoas=pessoas, ordem='id')

@app.route('/insercao')
def insercao():
    return render_template('insercao.html')

@app.route('/salvar_insercao', methods=['POST'])
def salvar_insercao():
    nome = request.form.get('nome')
    idade = int(request.form.get('idade'))
    sexo = request.form.get('sexo')
    salario = request.form.get('salario')

    pessoa = Pessoa(nome, idade, sexo, salario)

    db.session.add(pessoa)
    db.session.commit()

    pessoas = Pessoa.query.all()
    return render_template('listagem.html', pessoas=pessoas, ordem='id')

@app.route('/edicao/<int:id>')
def edicao(id=0):
    pessoa = Pessoa.query.filter_by(id=id).first()
    return render_template('edicao.html', pessoa=pessoa)

@app.route('/salvar_edicao', methods=['POST'])
def salvar_edicao():
    id = int(request.form.get('id'))
    nome = request.form.get('nome')
    idade = int(request.form.get('idade'))
    sexo = request.form.get('sexo')
    salario = request.form.get('salario')

    pessoa = Pessoa.query.filter_by(id=id).first()

    pessoa.nome = nome
    pessoa.idade = idade
    pessoa.sexo = sexo
    pessoa.salario = salario
    db.session.commit()

    pessoas = Pessoa.query.all()
    return render_template('listagem.html', pessoas=pessoas, ordem='id')

@app.route('/deletar/<int:id>')
def deletar(id=0):
    pessoa = Pessoa.query.filter_by(id=id).first()
    return render_template('deletar.html', pessoa=pessoa)

@app.route('/salvar_delecao', methods=['POST'])
def salvar_delecao():
    id = int(request.form.get('id'))

    pessoa = Pessoa.query.filter_by(id=id).first()

    db.session.delete(pessoa)
    db.session.commit()

    pessoas = Pessoa.query.all()
    return render_template('listagem.html', pessoas=pessoas, ordem='id')

@app.route('/graficos')
def graficos():
    pessoasM = Pessoa.query.filter_by(sexo='M').all()
    pessoasF = Pessoa.query.filter_by(sexo='F').all()

    salarioM = 0
    for m in pessoasM:
        salarioM += m.salario
    if len(pessoasM) > 0:
        salarioM = salarioM / len(pessoasM)

    salarioF = 0
    for f in pessoasF:
        salarioF += f.salario
    if len(pessoasF) > 0:
        salarioF = salarioF / len(pessoasF)

    idadeM = 0
    for m in pessoasM:
        idadeM += m.salario
    if len(pessoasM) > 0:
        idadeM = idadeM / len(pessoasM)

    idadeF = 0
    for f in pessoasF:
        idadeF += f.salario
    if len(pessoasF) > 0:
        idadeF = idadeF / len(pessoasF)

    return render_template('graficos.html', salarioM=salarioM, salarioF=salarioF, idadeM=idadeM, idadeF=idadeF)