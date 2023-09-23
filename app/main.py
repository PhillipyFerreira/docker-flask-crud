'''
Created on Sep 10, 2017

@author: Pavan Aleti
'''

from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.database import Database


app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()
#Aqui deve ter um monitoramento de Four Golden Signal por endpoint
@app.route('/') 
def index():
    data = db.read(None)
 # Inserir métrica de Logging
    return render_template('index.html', data = data)
#Aqui deve ter um monitoramento de Four Golden Signal por endpoint
@app.route('/add/') 
def add():
    return render_template('add.html')
#Aqui deve ter um monitoramento de Four Golden Signal por endpoint
@app.route('/addphone', methods = ['POST', 'GET']) #Aqui deve ter um monitoramento de Golden Signal
def addphone():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("A new phone number has been added")
        else:
            flash("A new phone number can not be added")
 # Inserir métrica de Logging
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
#Aqui deve ter um monitoramento de Four Golden Signal por endpoint
@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);
 # Inserir métrica de Logging
    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)
#Aqui deve ter um monitoramento de Four Golden Signal por endpoint
@app.route('/updatephone', methods = ['POST'])
def updatephone():
    if request.method == 'POST' and request.form['update']:
 # Inserir monitoramento de Tracing
        if db.update(session['update'], request.form):
            flash('A phone number has been updated')
 # Inserir métrica de Logging
        else:
            flash('A phone number can not be updated')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
#Aqui deve ter um monitoramento de Four Golden Signal por endpoint
@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)
#Aqui deve ter um monitoramento de Four Golden Signal por endpoint
@app.route('/deletephone', methods = ['POST'])
def deletephone():
    if request.method == 'POST' and request.form['delete']:
  # Inserir monitoramento de Tracing
        if db.delete(session['delete']):
            flash('A phone number has been deleted')

        else:
            flash('A phone number can not be deleted')

        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
