#!/usr/bin/python3
import pymysql
db=pymysql.connect("localhost","root","","shopeazy")
mycursor=db.cursor()
sql="SELECT * FROM product"
mycursor.execute(sql)
data = mycursor.fetchall()
from texttable import Texttable
t = Texttable()
count=0
for row in data :
    t.add_rows([['ProductID',row[0]],['Description',row[1]],['Image',row[2]],['Price',row[3]],['UserName',row[4]]])
    count+=1
    print ("\n\n <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TABLE",count,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")
    print (t.draw())
