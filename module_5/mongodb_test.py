""" 
    mongodb_test.py test code
    Anthony Nebel
    10 April 2021
    Test program for connecting to a MongoDB Atlas cluster
"""
# https://github.com/AnthonyNebel/csd-310.git

from pymongo import MongoClient


url = "mongodb+srv://admin:admin@cluster0.djd2z.mongodb.net/pytech?retryWrites=true&w=majority"


client = MongoClient(url)

db = client.pytech


print("\n -- Pytech COllection List --")
print(db.list_collection_names())


input("\n\n  End of program, press any key to exit... ")