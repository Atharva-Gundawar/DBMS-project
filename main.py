import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="atharva.n.gundawar@gmail.com",
  password="Hs5:HY2mdTrRbNw"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)