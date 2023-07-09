#import statements
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://admin:admin@cluster0.4eilq7t.mongodb.net/?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"
client = MongoClient(uri)
db = client.pytech
students = db.students

#find all students in students collection
student_list = students.find({})

#display message
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#retrieve collection and output results
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#find document by student_id
bella = students.find_one({"student_id": "1008"})

#output results
print("\n -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + bella["student_id"] + "\n  First Name: " + bella["first_name"] + "\n  Last Name: " + bella["last_name"] + "\n")

#exit message
input("\n\n  End of program, press any key to continue...")

