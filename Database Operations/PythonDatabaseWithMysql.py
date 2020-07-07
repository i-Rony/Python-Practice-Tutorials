import pymysql

#Database connection

def getConnection() :
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="the_programming_guy")    
    return connection


# Create table 
connection = pymysql.connect(host="localhost",user="root",passwd="",database="the_programming_guy")
cursor = connection.cursor()
sql_create_table ="create table person(id int(20) primary key auto_increment, firstname char(20) not null,lastname char(20) not null)"
cursor.execute(sql_create_table)
connection.close()

# Insert Data
conn = getConnection()
cursor = conn.cursor()
i1 = "insert into person(firstname,lastname) values ('Nancymaria','Arulraj')"
i2 = "insert into person(firstname,lastname) values ('Paul','Coulson')"
cursor.execute(i1)
cursor.execute(i2)
conn.commit()
cursor.close()

# Update Data
conn = getConnection()
cursor = conn.cursor()
sql_update_record ="update person set firstname='Nancy' where id =102"
cursor.execute(sql_update_record)
conn.commit()
cursor.close()
print("File Updated Successfully....")

#Delete  Data
conn = getConnection()
cursor = conn.cursor()
sql_delete_record ="delete from person where id =102"
cursor.execute(sql_delete_record)
conn.commit()
cursor.close()
print("Record Deleted Successfully....")

# Fetch Data 
conn = getConnection()
cursor = conn.cursor()
sql_fetch_persons ="select * from person"
cursor.execute(sql_fetch_persons)
for row in cursor.fetchall() :
    print(row)
cursor.close()