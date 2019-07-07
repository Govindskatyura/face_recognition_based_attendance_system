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

'''
class connector:
    def __init__(self):
        self.myDB=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="facedatabase"
            )
    def __dis__(self):
        self.myDB.close()
    def executeQuery(self,query):
        self.mycursor=self.myDB.cursor()
        self.mycursor=self.mycursor.execute(query)
        if self.mycursor is not None:
            return(self.mycursor[0])
        self.myDB.commit()
        #self.__dis__()
    def getData(self,query):
        self.mycursor = self.myDB.cursor()
        self.mycursor.execute("SELECT * FROM attandance")
        self.all_list=self.mycursor.fetchall()
        #print(all_list)
        #mydb.close
        return self.all_list

'''