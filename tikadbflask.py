from pymongo import MongoClient

# MongoDB'ye bağlan
client = MongoClient('mongodb+srv://TikaDB:4Qx2Z4KXoHWCAE1a@cluster0.3gvxv8u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

# 'mydatabase' adında bir veritabanı seç
db = client['mydatabase']

# 'mycollection' adında bir koleksiyon seç
collection = db['mycollection']

# Bir belge ekle
document = {"name": "Alice", "age": 30, "city": "New York"}
insert_result = collection.insert_one(document)
print(f"Eklenen belgenin id'si: {insert_result.inserted_id}")

# Bir belge bul
found_document = collection.find_one({"name": "Alice"})
print(f"Bulunan belge: {found_document}")
