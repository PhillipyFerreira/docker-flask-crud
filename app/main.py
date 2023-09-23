'''
Created on Sep 10, 2017

@author: Pavan Aleti
'''

from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.database import Database
from prometheus_flask_exporter import PrometheusMetrics
from opentelemetry.instrumentation.flask import FlaskInstrumentor
import logging


app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()
metrics = PrometheusMetrics(app)
FlaskInstrumentor().instrument_app(app)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app.config.from_pyfile('tracing_config.py')

@app.route('/') # Four Golden Signal / TRACING
def index():
    data = db.read(None)
    logger.info("'/' route accessed")
    return render_template('index.html', data = data)

@app.route('/add/') # Four Golden Signal / TRACING
def add():
    logger.info("'/add/' route accessed")
    return render_template('add.html')

@app.route('/addphone', methods = ['POST', 'GET']) # Four Golden Signal / TRACING
def addphone():
    logger.info("'/addphone' route accessed with %s request", request.method)
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("A new phone number has been added") # LOG: INFO
            logger.info("A phone number has been added")
        else:
            flash("A new phone number can not be added") # LOG: WARNING
            logger.warning("A phone number couldn't be added")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/update/<int:id>/') # Four Golden Signal / TRACING
def update(id):
    logger.info("'/update/<int:id>/' route accessed with %s request", id)
    data = db.read(id);

    if len(data) == 0:
        logger.warning("Id not found!")
        return redirect(url_for('index'))
    else:
        session['update'] = id
        logger.info("A phone number has been updated")
        return render_template('update.html', data = data)

@app.route('/updatephone', methods = ['POST']) # Four Golden Signal / TRACING
def updatephone():
    logger.info("'/updatephone' route accessed with %s method", request.method)
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('A phone number has been updated') # LOG: INFO
            logger.info("A phone number has been updated")

        else:
            flash('A phone number can not be updated') # LOG: WARNING
            logger.warning("Could not update phone number")

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/delete/<int:id>/') # Four Golden Signal / TRACING
def delete(id):
    logger.info("'/delete/' route accessed with id %s", id)
    data = db.read(id);

    if len(data) == 0:
        logger.warning("Id not found!")
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        logger.info("A phone number has been deleted")
        return render_template('delete.html', data = data)

@app.route('/deletephone', methods = ['POST']) # Four Golden Signal / TRACING 
def deletephone():
    logger.info("'/deletephone' route accessed with %s method", request.method)
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('A phone number has been deleted') # LOG: INFO
            logger.info("A phone number has been deleted")

        else:
            flash('A phone number can not be deleted') # LOG: WARNING
            logger.warning("Could not delete phone!")

        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    ogger.warning("Could not find page!")
    return render_template('error.html') # LOG: WARNING

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0") # LOG: INFO
