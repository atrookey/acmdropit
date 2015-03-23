from flask import Flask, render_template
import pymongo

app = Flask(__name__)

MONGODB_URI = 'mongodb://heroku_app35160490:n52q2opnmfvpluv4rvvfthi2p4@ds035240.mongolab.com:35240/heroku_app35160490'

client = pymongo.MongoClient(MONGODB_URI)
db = client.get_default_database()

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

if __name__ == '__main__':
  app.run()