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

#Update student id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Cullen II"}})

#find student doc 1007
edward = students.find_one({"student_id": "1007"})

#Display message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

#output message
print("  Student ID: " + edward["student_id"] + "\n  First Name: " + edward["first_name"] + "\n  Last Name: " + edward["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")