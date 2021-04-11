""" 
    Pytech: Collection Queries. pytech_insert.py program
    Anthony Nebel
    10 April 2021
    Program that inserts student records into the pytech students collection
"""
# https://github.com/AnthonyNebel/csd-310.git

from pymongo import MongoClient


url = "mongodb+srv://admin:admin@cluster0.djd2z.mongodb.net/pytech?retry\
	Writes=true&w=majority"
client = MongoClient(url)
db = client.pytech

tony = {
    "student_id": "1007",
    "first_name": "Tony",
    "last_name": "Nebel",
    "enrollments": [
        {
            "term": "spring",
            "gpa": "4.0",
            "start_date": "March 15, 2021",
            "end_date": "May 16, 2021",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Soriano",
                    "grade": "4.0"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Payne",
                    "grade": "4.0"
                }
            ]
        }
    ]

}

lindsay = {
    "student_id": "1008",
    "first_name": "Lindsay",
    "last_name": "Nebel",
    "enrollments": [
        {
            "term": "spring",
            "gpa": "3.9",
            "start_date": "March 15, 2021",
            "end_date": "May 16, 2021",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Soriano",
                    "grade": "3.8"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Payne",
                    "grade": "4.0"
                }
            ]
        }
    ]
}

alex = {
    "student_id": "1009",
    "first_name": "Alex",
    "last_name": "Nebel",
    "enrollments": [
        {
            "term": "spring",
            "gpa": "3.2",
            "start_date": "March 15, 2021",
            "end_date": "May 16, 2021",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Soriano",
                    "grade": "3.3"
                },
                {
                    "course_id": "CSD 320",
                    "description": "Programming with Java",
                    "instructor": "Payne",
                    "grade": "3.1"
                }
            ]
        }
    ]
}

students = db.students

print("\n  -- INSERT STATEMENTS --")

tony_student_id = students.insert_one(tony).inserted_id
print("  Inserted student record Tony Nebel into the students collection with document_id " + str(tony_student_id))

lindsay_student_id = students.insert_one(lindsay).inserted_id
print("  Inserted student record Linday Nebel into the students collection with document_id " + str(lindsay_student_id))

alex_student_id = students.insert_one(alex).inserted_id
print("  Inserted student record Alex Nebel into the students collection with document_id " + str(alex_student_id))

input("\n\n  End of program, press any key to exit... ")