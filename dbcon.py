import mysql.connector
def con(query):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="facedatabase"
    )
    mycursor = mydb.cursor()
    #print(query)
    mycursor.execute(query)
    mycursor=mycursor.fetchone()
    if mycursor is  not None :
        return(mycursor[0])
    mydb.commit()
    mydb.close


def attandace(people):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="facedatabase"
    )
    mycursor = mydb.cursor()
    batch=con("SELECT class FROM studentinfp WHERE username='%s'" %people)
    mycursor.execute("INSERT INTO attandance (username, batch) VALUES ('%s','%s')" % (people,batch))
    mydb.commit()
    mydb.close

def showall():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="facedatabase"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM attandance")
    all_list=mycursor.fetchall()
    #print(all_list)
    mydb.close
    return all_list
