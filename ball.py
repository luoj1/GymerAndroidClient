import MySQLdb
import pandas as pd
db = MySQLdb.connect(host="localhost",user="gtapp",passwd="Git!hacks2018s",db="apphacks")
cur=db.cursor()

def create():
    sql="""CREATE TABLE GYM (
             ID  INT NOT NULL AUTO_INCREMENT,
             NAME  CHAR(20),
             GYM   CHAR(20),  
             TYPE  CHAR(20),
             TIMES CHAR(20),
             TIMEE CHAR(20),
             COMMENT CHAR(100)"""
    cur.execute(sql)

def insert(name,gym,tp,times,timee, comments):   
    sql = "INSERT INTO GYM ( 'NAME', 'GYM', 'TYPE',  'TIMES', 'TIMEE, 'COMMENTS') VALUES('%s','%s','%s','%s','%s','%s')"
    ( name,gym,tp,times,timee, comments )
    try:
        cur.execute(sql)
        db.commit()
    except:
       db.rollback()


def delete(name):
    sql = "DELETE FROM GYM WHERE NAME=="+name
    try:
        cur.execute(sql)
        db.commit()
    except:
       db.rollback()

    
def update(name,gym,tp,times,timee, comments):
    sql = "UPDATE GYM ( 'NAME', 'GYM', 'TYPE',  'TIMES', 'TIMEE, 'COMMENTS') VALUES('%s','%s','%s','%s','%s','%s')"
    ( name,gym,tp,times,timee, comments )
    try:
        cur.execute(sql)
        db.commit()
    except:
       db.rollback()

def connect(file):
    
	return name,gym,tp,times,timee, comments

def main():
    file=open()
    (name,gym,tp,times,timee, comments)= connect(file)
    sql= 'SELECT * FROM GAMEAPP WHERE Name=='+name
    try:
        # Execute the SQL command
       cur.execute(sql)
       # Fetch all the rows in a list of lists.
       ls= cur.fetchall()
    except:
        print('Error!!!')
    if ls==(): 
    	insert(name,gym,tp,times,timee, comments)
    else:
        a= input('whether you should update the value of delete the data? (U/D/N)')
        a=a.upper()
        if a=='U':
            update(name,gym,tp,times,timee, comments)
        elif a=='D':
            delete(name)
    df=pd.read_sql('SELECT * FROM GAMEAPP;', con= db)
    db.close()
    
main()