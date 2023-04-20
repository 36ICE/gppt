from db.mongo_utils import MongoDB

#mongo_uri = 'mongodb://username:password@localhost:27017'
mongo = MongoDB("mongodb://localhost:27017/")
db_name = "my_database"
collection_name = "my_collection"

# 插入单个文档
result = mongo.insert_one(db_name, collection_name, {"name": "Alice", "age": 25})
print(result.inserted_id)

# 插入多个文档
documents = [{"name": "Bob", "age": 30}, {"name": "Charlie", "age": 35}]
result = mongo.insert_many(db_name, collection_name, documents)
print(result.inserted_ids)

# 查询单个文档
query = {"name": "Alice"}
result = mongo.find_one(db_name, collection_name, query)
print(result)

# 查询多个文档
query = {"age": {"$gt": 30}}
results = mongo.find_many(db_name, collection_name, query)
for result in results:
    print(result)

# 更新单个文档
query = {"name": "Alice"}
update = {"$set": {"age": 26}}
result = mongo.update_one(db_name, collection_name, query, update)
print(result.modified_count)

# 更新多个文档
query = {"age": {"$gt": 30}}
update = {"$inc": {"age": 1}}
result = mongo.update_many(db_name, collection_name, query, update)
print
