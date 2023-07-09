from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://admin:admin@cluster0.4eilq7t.mongodb.net/?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"

client = MongoClient(uri)

db = client.pytech

print("\n -- Pytech COllection List --")
print(db.list_collection_names())

input("\n\n  End of program, press any key to exit... ")
