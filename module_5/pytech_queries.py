""" 
    Pytech: Collection Queries. pytech_insert.py program
    Anthony Nebel
    10 April 2021
    Program that queries the student collection and displays record 1008
"""
# https://github.com/AnthonyNebel/csd-310.git

from pymongo import MongoClient


url = "mongodb+srv://admin:admin@cluster0.djd2z.mongodb.net/pytech?retry\
	Writes=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students
student_list = students.find({})


print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")


lindsay = students.find_one({"student_id": "1008"})


print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + lindsay["student_id"] + "\n  First Name: " + lindsay["first_name"] + "\n  Last Name: " + lindsay["last_name"] + "\n")

 
input("\n\n  End of program, press any key to continue...")