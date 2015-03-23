from flask import Flask, render_template
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def home():
  online_users = mongo.db.testData.find({'online': True})
  return render_template('home.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/quotes')
def contact():
  return render_template('quotes.html')

if __name__ == '__main__':
  app.run()