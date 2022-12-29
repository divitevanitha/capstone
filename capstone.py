import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'HCL-02-75\SQLEXPRESS'
database = 'FileSearchResults1'
username = 'vanitha'
password = 'Vanitha@123'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

print(cnxn)
cursor = cnxn.cursor()
print(cursor)

cursor.execute('''
                INSERT INTO FileSearchResults_table1 (File_Location, SearchCount, NameOfFile)
                VALUES
                ('C:\mainfolder\emptyfile.txt.txt',2,'emptyfile') ''')
cnxn.commit()

values=cursor.execute('select * from FileSearchResults_table1')
for i in values:
    print(i)