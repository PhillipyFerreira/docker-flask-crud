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
    #Implementação do four golden signal 
def index():
    #Implementação do four golden signal 
    data = db.read(None)
    # inserir logging.info
    return render_template('index.html', data = data)

@app.route('/add/')
    #Implementação do four golden signal 
def add():
    # inserir logging.info
    return render_template('add.html')

@app.route('/addphone', methods = ['POST', 'GET'])
    #Implementação do four golden signal 
def addphone():
    if request.method == 'POST' and request.form['save']:
        # inserir logging.info
        if db.insert(request.form):
            
            flash("A new phone number has been added")
        else:
            # inserir logging.warn
            flash("A new phone number can not be added")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/update/<int:id>/')
   #Implementação do four golden signal 
def update(id):
    # inserir logging.info
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)

@app.route('/updatephone', methods = ['POST'])
#Implementação do four golden signal 
def updatephone():
    if request.method == 'POST' and request.form['update']:
        # inserir logging.info
        if db.update(session['update'], request.form):
            flash('A phone number has been updated')

        else:
            # inserir logging.warn
            flash('A phone number can not be updated')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/delete/<int:id>/')
    #Implementação do four golden signal 
def delete(id):
    data = db.read(id);
    # inserir logging.info
    if len(data) == 0:
        # inserir logging.warn
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)

@app.route('/deletephone', methods = ['POST'])
    #Implementação do four golden signal 
def deletephone():
    if request.method == 'POST' and request.form['delete']:
        # inserir logging.info
        if db.delete(session['delete']):
            flash('A phone number has been deleted')

        else:
            # inserir logging.warn
            flash('A phone number can not be deleted')

        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
    #Implementação do four golden signal 
def page_not_found(error):
    # inserir logging.error
    return render_template('error.html')

if __name__ == '__main__':
    #inserir logging.info
    app.run(port=5000, host="0.0.0.0")
