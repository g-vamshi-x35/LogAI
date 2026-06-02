from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["logai_db"]

logs_collection = db["logs"]
reports_collection = db["reports"]
users_collection = db["users"]

print("mongo connected successfully!")


