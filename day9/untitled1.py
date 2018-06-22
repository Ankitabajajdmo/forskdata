import sqlalchemy
from pandas import DataFrame

engine=sqlalchemy.create_engine("mysql://root:@localhost/data science")
query = "select * from job_satisfaction" #query Database
resoverall = engine.execute(query) #execute Query
df = DataFrame(resoverall.fetchall()) #putting the result into Dataframe
df.columns = resoverall.keys() #Setting the Column names as it was in database.



from pandas import DataFrame
import mysql.connector

# connect to  MySQL server along with Database name
conn = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='job_satisfaction')

# Creating cursor Object from connection object
cursor = conn.cursor()

query = ("SELECT * FROM job_satisfaction;")  # query Database
cursor.execute(query)  # execute Query
df = DataFrame(cursor.fetchall())  # putting the result into Dataframe
df.columns = cursor.column_names  # Setting the Column names as it was in database.
