from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

MONGODB_URI = 'mongodb://heroku_app35160490:n52q2opnmfvpluv4rvvfthi2p4@ds035240.mongolab.com:35240/heroku_app35160490'
RANGE = 1

client = pymongo.MongoClient(MONGODB_URI)
db = client.get_default_database()

@app.route('/get_image', methods=['GET'])
def get_image():
  latitude = request.args.get('latitude')
  longitude = request.args.get('longitude')
  if(latitude == None or longitude == None):
    return jsonify({})
  latitude = float(latitude)
  longitude = float(longitude)
  lat_min = latitude - RANGE
  lat_max = latitude + RANGE
  long_min = longitude - RANGE
  long_max = longitude + RANGE
  image_doc = db.images.find_one({'latitude': { '$gt': lat_min, '$lt': lat_max },'longitude': { '$gt': long_min, '$lt': long_max }})
  if(image_doc == None):
    return jsonify({})
  db.images.remove({'_id':image_doc.get('_id')})
  return jsonify({'image': image_doc.get('image')})

@app.route('/store_image', methods=['POST'])
def store_image():
  latitude = request.form['latitude']
  longitude = request.form['longitude']
  image = request.form['image']
  latitude = float(latitude)
  longitude = float(longitude)
  post = {'latitude': latitude,
          'longitude': longitude,
          'image': image }
  db.images.insert(post)
  return 'post successful'

if __name__ == '__main__':
  app.run(debug=True)