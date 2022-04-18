import pymysql as p
def getconnection():
    return p.connect(host='localhost',user='root',password='',database='aniket')

def addData(t):
    db=getconnection()
    sql='insert into data values(%s,%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()


def loginvalidation(a):
    db=getconnection()
    sql="select * from data where Username=%s and Password=%s"
    cr=db.cursor()
    cr.execute(sql,a)
    users=cr.fetchall()
    db.commit()
    db.close()
    return users



    
