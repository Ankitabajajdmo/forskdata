import requests
url="https://api.mlab.com/api/1/databases/db_university/collections/students?apiKey=by3rDUxSEaqHvGfTBuz5tgws-PtsdQkw"
   
data = {
        "Student_Name" : input("Enter Student_Name: "),
        "Student_Age" : input("Enter Student_Age: "),
        "Student_Roll_no" : input("Student_Roll_no: "),
        "Student_Branch" : input("Enter Student_Branch: ")
        }

send = requests.post(url,json = data)
print(send.text)
