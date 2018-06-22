from pymongo import MongoClient
from datetime import datetime
#import json

client = MongoClient('localhost', 27017)
mydb = client.db_University

def add_client(Student_Name, Student_Age, Student_Roll_no, Student_Branch):
    unique_client = mydb.students.find_one({"Student_Roll_no":Student_Roll_no,"Student_Name":Student_Name}, {"_id":0})
    if unique_client:
        return "Client already exists"
    else:
        mydb.students.insert(
                {
                "Student_Name" : Student_Name,
                "Student_Age" : Student_Age,
                "Student_Roll_no" : Student_Roll_no,
                "Student_Branch" : Student_Branch,
                "Date-Time" : datetime.now()
                })
        return "Student added successfully"

def view_client(Student_Roll_no):
    user = mydb.students.find_one({"Student_Roll_no":Student_Roll_no}, {"_id":0})
    if user:
        Student_Name = user["Student_Name"]
        Student_Age = user["Student_Age"]
        Student_Roll_no = user["Student_Roll_no"]
        Student_Branch = user["Student_Branch"]
        time = user["Date-Time"]
        return {"Student_Name":Student_Name,"Student_Age":Student_Age,"Student_Roll_no":Student_Roll_no,"Student_Branch":Student_Branch}
    else:
        return "Sorry, No such student exists"
for i in range(10):
    Student_Name = input("Enter Student_Name: ")
    Student_Age = input("Enter Student_Age: ")
    Student_Roll_no = input("Student_Roll_no: ")
    Student_Branch =input("Enter Student_Branch: ")
    
    print(add_client(Student_Name,Student_Age,Student_Roll_no,Student_Branch))

user = input("Enter Student_Roll_no to find: ")
user_data = view_client(user)

print(user_data)