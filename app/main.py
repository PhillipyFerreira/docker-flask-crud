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
    # Inserir métrica de Logging
    data = db.read(None) 

    return render_template('index.html', data = data)
    # Inserir métrica Golden Signal

@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/addphone', methods = ['POST', 'GET'])
def addphone():
    # Inserir métrica de Logging
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("A new phone number has been added")
        else:
            flash("A new phone number can not be added")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
        # Inserir métrica Golden Signal
        # Inserir Tracing

@app.route('/update/<int:id>/')
def update(id):
    # Inserir métrica de Logging
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)
    # Inserir métrica Golden Signal
    # Inserir Tracing

@app.route('/updatephone', methods = ['POST'])
def updatephone():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('A phone number has been updated')

        else:
            flash('A phone number can not be updated')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
        # Inserir Tracing
        # Inserir métrica Golden Signal

@app.route('/delete/<int:id>/')
def delete(id):
    # Inserir métrica de Logging
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)
        # Inserir Tracing

@app.route('/deletephone', methods = ['POST'])
def deletephone():  
    # Inserir métrica de Logging
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('A phone number has been deleted')

        else:
            flash('A phone number can not be deleted')

        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
        # Inserir Tracing

@app.errorhandler(404)
def page_not_found(error):
    # Inserir métrica de Logging
    return render_template('error.html')

if __name__ == '__main__':
    # Inserir métrica de Logging
    app.run(port=5000, host="0.0.0.0")
