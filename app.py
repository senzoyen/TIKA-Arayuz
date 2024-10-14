from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB bağlantısı
client = MongoClient("mongodb+srv://TikaDB:4Qx2Z4KXoHWCAE1a@cluster0.3gvxv8u.mongodb.net/?retryWrites=true&w=majority")
db = client.mydatabase  # Kendi veritabanı adınızı kullanın
collection = db.data

@app.route('/api/data', methods=['POST'])
def add_data():
    data = request.json
    if data:
        collection.insert_one(data)
        return jsonify({"message": "Veri başarıyla kaydedildi"}), 201
    else:
        return jsonify({"message": "Geçersiz veri"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Tüm arayüzlerde 5000 portunda çalış
