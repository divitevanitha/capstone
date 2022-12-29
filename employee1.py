import pyodbc
server = 'HCL-02-75\SQLEXPRESS'
database = 'Employee'
username = 'vanitha'
password = 'Vanitha@123'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
"""query=('''create table Employee_info(
EMP_ID int NOT NULL, 
NAME varchar(30),
SALARY int,
PROJECT varchar(30)
PRIMARY KEY(EMP_ID))''')
cursor.execute(query)
cnxn.commit()"""

class HighBonusError(Exception):
    pass
class LessBonusError(Exception):
    pass
class Employee:
    Bonus = 2
    Projects = ['python','c','java']
    def insert_Employee_details(self,emp_id,name,Salary,project):
        query1 = ('''insert into Employee_info(emp_id,name,salary,project)
        values({0},'{1}',{2},'{3}')''')
        insertQuery1 = query1.format(emp_id,name,Salary,project)
        cursor.execute(insertQuery1)
        cursor.commit()
        print("inserted")
    def Display_Employee_Details(self):
        query2 = ('''select *from Employee_info ''')
        value=cursor.execute(query2)
        for i in value:
            print(i.EMP_ID,i.NAME,i.SALARY,i.PROJECT)
        print("displayed successfully")
    def add_bonus(self,name):
        try:
            bonus=int(input())
            if bonus>2:
                raise HighBonusError
            elif bonus<0:
                raise LessBonusError
            else:
                query = ''' select * from Employee_info where NAME='{}' '''
                searchquery = query.format(name)
                values = cursor.execute(searchquery)
                for b in values:
                    print(b)
                    oldsalary = b.Salary
                    newsalary = oldsalary * (1 + bonus)
                    print(newsalary)
                    query1 = ''' UPDATE Employee_info SET Salary={0} WHERE NAME='{1}' '''
                    query2 = query1.format(newsalary,name)
            # print(query2)
                    cursor.execute(query2)
            # print(query2)
                    cnxn.commit()

        except HighBonusError:
            print("bonus should not be gretarthan 2")
        except LessBonusError:
            print("bonus should not be less than 0")
    def update_salary(self):
        try:
            salary = 70000
            query = ''' select * from Employee_info where NAME='{}' '''
            searchquery = query.format(self.NAME)
            values = cursor.execute(searchquery)
            for i in values:
                oldsalary = i.Salary
                query = '''UPDATE Employee_info SET Salary={0} where NAME='{1}' '''
                query1 = query.format(salary, self.NAME)
                cursor.execute(query1)
                cnxn.commit()
        except:
            pass

obj=Employee()
obj.Display_Employee_Details()
obj.add_bonus("zion")
obj.update_salary()





