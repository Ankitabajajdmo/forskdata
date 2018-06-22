import json 
n=0
while n <2:
    n=int(input("enter n(n>=2): "))

faculty_list=[]
for i in range(n):
    faculty_member={
        "First Name":input("First Name : "),
        "last name" : input("last name : "),
        "photo":input("photo : "),
        "Department":input("Department : "),
        "research Areas":input("research Areas : ").split(","),
        "contact Details":[input("phone no : "),input("address : ")]
        }
    faculty_list.append(faculty_member)
    

filename = "ank"      
f = open(filename + "_jsonFile.txt", "w")  # SAVING DATA TO FILE
json.dump(faculty_list,f)
f.close()
print(faculty_list)
