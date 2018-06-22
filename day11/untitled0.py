import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')
    
### For each of these three tables, find the number of rows in the table and
### the number of unique students in the table. To find the number of unique
### students, you might want to create a set of the account keys in each table.

enrollment_num_rows = len(enrollments)            # Replace this with your code
enrollment_num_unique_students = set( ) # Replace this with your code
for enrollment in enrollments:
    enrollment_num_unique_students.add(enrollment["account_key"])
    
len (enrollment_num_unique_students)
    
    
engagement_num_rows =len(daily_engagement)             # Replace this with your code
engagement_num_unique_students = 0  # Replace this with your code

submission_num_rows = len(project_submissions)             # Replace this with your code
submission_num_unique_students = 0  # Replace this with your code