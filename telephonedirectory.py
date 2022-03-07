# -*- coding: utf-8 -*-
"""telephonedirectory.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ho5ZxVvMgISJtHXtpomcPfITX0tabVF4
"""

import pymongo

# Telephone directory and curd operation

#creating a database

data = pymongo.MongoClient("mongodb://Atharva1999:GUVI@cluster0-shard-00-00.q3cbh.mongodb.net:27017,cluster0-shard-00-01.q3cbh.mongodb.net:27017,cluster0-shard-00-02.q3cbh.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-69y0v0-shard-0&authSource=admin&retryWrites=true&w=majority")

db = data["TELEPHONE_DIRECTORY"]

# Creating Collections

a = db["Directory"]

# Inserting Records into the collections

a.insert_many([{"Name":"Atharva","Phone_number":123456789,"location":"Mumbai","Age":21},{"Name":"josep","Phone_number":122256789,"location":"Pune","Age":22},{"Name":"Subhash","Phone_number":123454589,"location":"Mumbai","Age":23},{"Name":"mangesh","Phone_number":123451989,"location":"Mumbai","Age":20},{"Name":"Haldiram","Phone_number":121116789,"location":"Nagpur","Age":40},{"Name":"Sula","Phone_number":1232226789,"location":"Nashik","Age":30},{"Name":"Anil","Phone_number":123333789,"location":"Mumbai","Age":33},{"Name":"Deepkia","Phone_number":128886789,"location":"Delhi","Age":44}])

# Modifying Records

a.update_one({"Name":"Anil"},{"$set":{"place":"Chennai"}})

for item in a.find():
  print(item)

