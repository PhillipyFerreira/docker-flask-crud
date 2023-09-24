'''
Created on Sep 10, 2017

@author: Pavan Aleti
'''

from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.database import Database


app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()

@app.route('/') #Four Golden Signal of Monitoring e Tracing
def index():
    data = db.read(None)

    return render_template('index.html', data = data)

@app.route('/add/') #Four Golden Signal of Monitoring e Tracing
def add():
    return render_template('add.html')

@app.route('/addphone', methods = ['POST', 'GET']) #Four Golden Signal of Monitoring e Tracing
def addphone():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("A new phone number has been added") 
        else:
            flash("A new phone number can not be added") # Warning -> LOG pois é um evento potencialmente problemático ou e deve ser monitorado.

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/update/<int:id>/') #Four Golden Signal of Monitoring e Tracing
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)

@app.route('/updatephone', methods = ['POST']) #Four Golden Signal of Monitoring e Tracing
def updatephone():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('A phone number has been updated')

        else:
            flash('A phone number can not be updated') # Warning -> LOG pois é um evento potencialmente problemático ou e deve ser monitorado.

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/delete/<int:id>/') #Four Golden Signal of Monitoring e Tracing
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)

@app.route('/deletephone', methods = ['POST']) #Four Golden Signal of Monitoring e Tracing
def deletephone():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('A phone number has been deleted')

        else:
            flash('A phone number can not be deleted') # Warning -> LOG pois é um evento potencialmente problemático ou e deve ser monitorado.

        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html') # Fiquei na duvida de qual é mas creio que seja Error -> LOG pois é um erro que não impede o funcionamento e precisa de atenção

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0") # Info -> LOG
