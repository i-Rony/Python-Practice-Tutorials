import pymysql
con=pymysql.connect(host="localhost", user="root", password="", db="crud")

curser=con.cursor()

#Inserting data into database
#curser.execute("insert into record(id,name) values('2','Atif');")
#print("Data Inserted!")

#Updating data in database
#curser.execute("update record set name='Zia' where id='2'")
#print("Updated!")

#Deleting data from database
#curser.execute("delete from record where name='Zia'")
#print("Record Deleted!")

#Fetching data from database
#curser.execute("select * from record")
#print(curser.fetchall())


con.commit()
con.close()