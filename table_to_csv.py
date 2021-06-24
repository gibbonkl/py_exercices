from mysql.connector import connect
import pandas as pd 

# connecting to db
conn = connect(host = "localhost",user = "root", password = "", db= "testdb") 
cursor = conn.cursor()

# insert into db
'''
cursor.execute("insert into testtable values ('dfo7','9bn7')")
conn.commit()
'''

# select from db
cursor.execute('select * from testtable')
table_content = cursor.fetchall()

# table content to csv file
pd.DataFrame(table_content).to_csv('table_content.csv', index=False)