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

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " +\
    	doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

kenzie = {
    "student_id": "1010",
    "first_name": "Kenzie",
    "last_name": "Nebel"
}

kenzie_id = students.insert_one(kenzie).inserted_id
 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with\
	document_id " + str(kenzie_id))

student_kenzie = students.find_one({"student_id": "1010"})

print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_kenzie["student_id"] + "\n  First Name: " +\
	student_kenzie["first_name"] + "\n  Last Name: " +\
	student_kenzie["last_name"] + "\n")

deleted_student_kenzie = students.delete_one({"student_id": "1010"})

new_student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
 
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " +\
    	doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

input("\n\n  End of program, press any key to continue...")