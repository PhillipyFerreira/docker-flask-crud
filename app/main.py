'''
Created on Sep 10, 2017

@author: Pavan Aleti
'''

from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.database import Database


app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()

# Four Golden Signal por endpoint: 
#Pode adicionar métricas de latência (tempo de execução); 
#erros (contagem de erros);
#taxa de tráfego (Quantidade de solicitações por unidade de tempo);
#e saturação (utilização de recursos)
@app.route('/')
def index():
    # Four Golden Signal: Medir latência (tempo de execução)
    data = db.read(None)

    return render_template('index.html', data = data)

# Inclusão de logs de níveis DEBUG, INFO, WARN, ERROR e FATAL:
@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/addphone', methods = ['POST', 'GET'])
def addphone():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("A new phone number has been added")
        else:
            flash("A new phone number can not be added")

        # logging INFO para registrar ação bem-sucedida

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)

@app.route('/updatephone', methods = ['POST'])
def updatephone():
    if request.method == 'POST' and request.form['update']:
        #logging DEBUNG para rastrear eventos de atualização
 
        if db.update(session['update'], request.form):
            flash('A phone number has been updated')
        #logging ERROR pararegistrar erros de atualização 
        else:
            flash('A phone number can not be updated')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)

@app.route('/deletephone', methods = ['POST'])
def deletephone():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('A phone number has been deleted')
            #logging INFO para registrar ação bem-sucedida 
        else:
            flash('A phone number can not be deleted')
            #logging ERROR para registrar erros de exclusão 
        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    #Tracing
    # Inclusão de logs: configuração de logging
    app.run(port=5000, host="0.0.0.0")
