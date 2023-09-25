'''
Created on Sep 10, 2017

@author: Pavan Aleti
'''

from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.database import Database


app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()

# Inclusão de logging de INFO.
@app.route('/')
def index():
    data = db.read(None)
    
# Inclusão de logging de INFO.
    return render_template('index.html', data = data)

# Inclusão de logging de INFO.
@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/addphone', methods = ['POST', 'GET'])

# Four Golden Signal (Latência, Tráfico e Saturação)
# Inclusão de logging de INFO.
def addphone():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("A new phone number has been added")
        else:
            # Four Golden Signal (Erro)
            # Inclusão de logging de ERROR.
            flash("A new phone number can not be added")

        # Inclusão de logging de INFO.
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

# Four Golden Signal (Latência, Tráfico e Saturação)
# Inclusão de logging de INFO.
@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);

    # Inclusão de logging de WARNING.
    # Inclusão de logging de INFO.
    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        # Inclusão de logging de INFO.
        session['update'] = id
        return render_template('update.html', data = data)

@app.route('/updatephone', methods = ['POST'])
def updatephone():
    # Four Golden Signal (Latência, Tráfico e Saturação)
    # Inclusão de logging de INFO.
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('A phone number has been updated')

        # Four Golden Signal (Erro)
        # Inclusão de logging de ERROR.   
        else:
            flash('A phone number can not be updated')

        session.pop('update', None)

        # Inclusão de logging de INFO.
        return redirect(url_for('index'))
    else:
        # Inclusão de logging de INFO.
        return redirect(url_for('index'))

@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    # Inclusão de logging de INFO.
    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        # Inclusão de logging de INFO.
        session['delete'] = id
        return render_template('delete.html', data = data)

@app.route('/deletephone', methods = ['POST'])
def deletephone():
    # Four Golden Signal (Latência, Tráfico e Saturação)
    # Inclusão de logging de INFO.
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('A phone number has been deleted')

        # Four Golden Signal (Erro)
        # Inclusão de logging de ERROR.
        else:
            flash('A phone number can not be deleted')

        session.pop('delete', None)

        # Inclusão de logging de INFO.
        return redirect(url_for('index'))
    else:
        # Inclusão de logging de INFO.
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    # Inclusão de logging de WARNING.
    # Inclusão de logging de INFO.
    return render_template('error.html')

if __name__ == '__main__':
    # Inclusão de logging de INFO.
    app.run(port=5000, host="0.0.0.0")
