import pyodbc
'''
def read(cntn):
      curs = cntn.cursor()
      curs.execute('select * from dbo.UserRelated')
      for row in curs:
            print('row = %r' %(row,) )
            print()
''' 
cntn=pyodbc.connect('Driver={SQL Server};Server=LAPTOP-DG9KS6R0\SQLEXPRESS2019;Database=Buddydb;Trusted_Connection=yes;')

'''
def insert():
         print("INSERTING DATA INTO THE TABLE")
         cur = cntn.cursor()
         uname = entryname.get()
         usecase = entry.get()
         sql = "INSERT INTO dbo.UserRelated VALUES(%s,%s)"
         cur.execute(sql,(uname,usecase))
         cntn.commit()
         read()
'''


#inserting data into the database
'''
cur = cntn.cursor()
cur.execute( " INSERT into dbo.UserRelated(id,username, usepuporrelation) values(?,?,?);", (3,"jordan", "machine sindane"))
cntn.commit()
'''
#################### RANDOM SELECT

def read(cntn):

    cur = cntn.cursor()
    
    lst = []
   
    cur.execute('SELECT id,questions from dbo.mathquestions')
    for row in cur:
       string =  f'{row}'
       lst.append(string)
    return lst
    '''

    import random
    lst = [1,2,3,4,5,6,7,8,9,10]
    sel = []
    for i in range(5):
        a = random.choice(lst)
        sel.append(a)

    crs = cntn.cursor()
    for i in sel
        crs.execute("SELECT * from dbo.mathdata where id = i")

    for row in crs:
            p = 'row = %r' %(row,)   
    
            
        ''' 
'''    
p=  read(cntn)
#select 
print(p)
'''
'''
num = 5
curs = cntn.cursor()
curs.execute('SELECT * from dbo.UserRelated where id='+str(num))
for row in curs:
    print( 'row =%r' %(row,))
 '''   
'''
# define new database
mycurse = cntn.cursor()

mycurse.execute("CREATE TABLE Matheq (expression VARCHAR(255), attempts int(10), num_correct int(5), num_failure int(5), routable VARCHAR(15), equationId int PRIMARY KEY AUTO_INCREMENT)")
'''

cntn.close()
################# selectfirst index
'''
strng = "we love maths"
p = strng[0]
print(p)
'''
'''
'''
'''
#show table in database

cur = cntn.cursor()
cur.executee("SHOW TABLES")
for tb in cur:
    print(tb)


'''