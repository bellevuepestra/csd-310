#import statements
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://admin:admin@cluster0.4eilq7t.mongodb.net/?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"
client = MongoClient(uri)
db = client.pytech
students = db.students

#student 1
edward = {
    "student_id": "1007",
    "first_name": "Edward",
    "last_name": "Cullen",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "A+"
                }
            ]
        }
    ]
}


#student 2
bella = {
    "student_id": "1008",
    "first_name": "Bella",
    "last_name": "Swan",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.52",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "B+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "A-"
                }
            ]
        }
    ]
}


#student 3
jacob = {
    "student_id": "1009",
    "first_name": "Jacob",
    "last_name": "Black",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "1.5",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "C"
                },
                {
                    "course_id": "CSD 320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "B"
                }
            ]
        }
    ]
}


#output
print("\n  -- INSERT STATEMENTS --")
edward_student_id = students.insert_one(edward).inserted_id
print("  Inserted student record Edward Cullen into the students collection with document_id " + str(edward_student_id))

bella_student_id = students.insert_one(bella).inserted_id
print("  Inserted student record Bella Swan into the students collection with document_id " + str(bella_student_id))

jacob_student_id = students.insert_one(jacob).inserted_id
print("  Inserted student record Jacob Black into the students collection with document_id " + str(jacob_student_id))

input("\n\n  End of program, press any key to exit... ")