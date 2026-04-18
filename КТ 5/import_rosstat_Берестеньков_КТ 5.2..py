import pandas as pd
from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:5000,localhost:5001,localhost:5002,localhost:5003,localhost:5004,localhost:5005,localhost:5006/?replicaSet=rs"
)

db = client["rosstat"]
collection = db["economy"]

file_path = "economy.xlsx"

df = pd.read_excel(file_path)

df.columns = df.columns.map(str)

print("Первые строки файла:")
print(df.head())

records = df.to_dict(orient="records")

if records:
    collection.insert_many(records)
    print(f"Загружено документов: {len(records)}")
else:
    print("Файл пуст")

print("Всего документов в коллекции:", collection.count_documents({}))
