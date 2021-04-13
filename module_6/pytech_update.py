""" 
    Pytech: Updating Documents. pytech_update.py program
    Anthony Nebel
    12 April 2021
    Program the updates the pytech students collection
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

result = students.update_one({"student_id": "1007"}, {"$set":\
	{"last_name": "Harrinton"}})

for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " +\
    	doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

tony = students.find_one({"student_id": "1007"})

print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

print("  Student ID: " + tony["student_id"] + "\n  First Name: " +\
	tony["first_name"] + "\n  Last Name: " + tony["last_name"] + "\n")

input("\n\n  End of program, press any key to continue...")