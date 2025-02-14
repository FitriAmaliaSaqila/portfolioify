import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)

@app.route('/') 
def home():
     return render_template('index.html')

@app.route("/contact", methods=["POST"])
def contact_post():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    doc = {
        'name': name,
        'email': email,
        'message': message
    }
    db.contacts.insert_one(doc)
    return jsonify({'msg': 'Pesan terkirim!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)