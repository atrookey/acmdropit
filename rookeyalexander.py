from flask import Flask, render_template
import pymongo

app = Flask(__name__)

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