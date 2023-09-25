'''
Created on Sep 10, 2017

@author: Pavan Aleti
'''

from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.database import Database

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()

@app.route('/')
def index():
    #Logging - INFO - Rota /..
    data = db.read(None)

    #Logging - INFO - Rota / - Rendezirar página index.html.
    return render_template('index.html', data = data)

@app.route('/add/')
def add():
    #Logging - INFO - Rota / - Rendezirar página add.html.
    return render_template('add.html')

@app.route('/addphone', methods = ['POST', 'GET'])
def addphone():
    #Four Golden Signal - Latência/Tráfico/Saturação
    #Logging - INFO - Rota /addphone.
    if request.method == 'POST' and request.form['save']:
        #Logging - INFO - Rota /addphone - Método POST a partir do botão SAVE.
        #Logging - INFO - Rota /addphone - Tentativa de inserção de registro.
        if db.insert(request.form):
            #Logging - INFO - Rota /addphone - Registro inserido com sucesso.
            flash("A new phone number has been added")
        else:
            #Four Golden Signal - Erro
            #Logging - ERROR - Rota /addphone - Erro na inserção do registro.
            flash("A new phone number can not be added")
         #Logging - INFO - Rota /addphone - Redireciona para a página index.html.
        return redirect(url_for('index'))
    else:
        #Logging - INFO - Rota /addphone - Não atendeu a primeira premissa.
        #Logging - INFO - Rota /addphone - Redireciona para a página index.html.
        return redirect(url_for('index'))

@app.route('/update/<int:id>/')
def update(id):
    #Four Golden Signal - Latência/Tráfico/Saturação
    #Logging - INFO - Rota /update.
    data = db.read(id);
    #Logging - INFO - Rota /update - Avaliar se encontrou o registro pelo id.
    if len(data) == 0:
        #Logging - WARNING - Rota /update - Registro não encontrado.
        #Logging - INFO - Rota /update - Redireciona para a página index.html.
        return redirect(url_for('index'))
    else:
        #Logging - INFO - Rota /update - Posicionar no registro encontrado.
        session['update'] = id
        #Logging - INFO - Rota /update - Rendezirar página update.html informando os dados do registro.
        return render_template('update.html', data = data)

@app.route('/updatephone', methods = ['POST'])
def updatephone():
    #Four Golden Signal - Latência/Tráfico/Saturação
    #Logging - INFO - Rota /updatephone.
    if request.method == 'POST' and request.form['update']:
        #Logging - INFO - Rota /updatephone - Método POST a partir do botão UPDATE.
        if db.update(session['update'], request.form):
            #Logging - INFO - Rota /updatephone - Registro alterado com sucesso.
            flash('A phone number has been updated')
        else:
            #Four Golden Signal - Erro
            #Logging - ERROR - Rota /updatephone - Erro na alteração do registro.
            flash('A phone number can not be updated')

        session.pop('update', None)
        #Logging - INFO - Rota /updatephone - Redireciona para a página index.html.
        return redirect(url_for('index'))
    else:
        #Logging - INFO - Rota /updatephone - Não atendeu a primeira premissa.
        #Logging - INFO - Rota /updatephone - Redireciona para a página index.html.
        return redirect(url_for('index'))

@app.route('/delete/<int:id>/')
def delete(id):
    #Four Golden Signal - Latência/Tráfico/Saturação
    #Logging - INFO - Rota /delete.
    data = db.read(id);

    #Logging - INFO - Rota /delete - Avaliar se encontrou o registro pelo id.
    if len(data) == 0:
        #Logging - WARNING - Rota /delete - Registro não encontrado.
        #Logging - INFO - Rota /delete - Redireciona para a página index.html.
        return redirect(url_for('index'))
    else:
        #Logging - INFO - Rota /delete - Posicionar no registro encontrado.
        session['delete'] = id
        #Logging - INFO - Rota /delete - Rendezirar página delete.html informando os dados do registro.
        return render_template('delete.html', data = data)

@app.route('/deletephone', methods = ['POST'])
def deletephone():
    #Four Golden Signal - Latência/Tráfico/Saturação
    #Logging - INFO - Rota /deletephone.
    if request.method == 'POST' and request.form['delete']:
        #Logging - INFO - Rota /deletephone - Método POST a partir do botão DELETE.
        if db.delete(session['delete']):
            #Logging - INFO - Rota /deletephone - Registro excluído com sucesso.
            flash('A phone number has been deleted')
        else:
            #Four Golden Signal - Erro
            #Logging - ERROR - Rota /deletephone - Erro na exlusão do registro.
            flash('A phone number can not be deleted')

        session.pop('delete', None)
        #Logging - INFO - Rota /deletephone - Redireciona para a página index.html.
        return redirect(url_for('index'))
    else:
        #Logging - INFO - Rota /deletephone - Não atendeu a primeira premissa.
        #Logging - INFO - Rota /deletephone - Redireciona para a página index.html.
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    #Logging - WARNING - Rota inexistente.
    #Logging - INFO - Rota inexistente rendezirar página error.html.
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
