#import statements
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://admin:admin@cluster0.4eilq7t.mongodb.net/?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"
client = MongoClient(uri)
db = client.pytech
students = db.students

#find all students in students collection
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#retrieve collection and output results
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# test doc
test_doc = {
    "student_id": "1010",
    "first_name": "John",
    "last_name": "Doe"
}

# insert test document into MongoDB atlas 
test_doc_id = students.insert_one(test_doc).inserted_id

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(test_doc_id))

# find_one() method by student id 1010
student_test_doc = students.find_one({"student_id": "1010"})

# display results 
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_test_doc["student_id"] + "\n  First Name: " + student_test_doc["first_name"] + "\n  Last Name: " + student_test_doc["last_name"] + "\n")

# delete_one method to remove the student_test_doc
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

# find all students in the collection 
new_student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# retrieve collection and output the results 
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")
