import pyodbc

server = 'HCL-02-75\SQLEXPRESS'
database = 'Employee_Schema'
username = 'vanitha'
password = 'Vanitha@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

class Insert_Error(Exception):
    def __str__(self):
        return "project is not in the list of projects"
class Id_Error(Exception):
    def __str__(self):
        return "Id already exist enter new id for employee"
class bonus_ex(Exception):
    def __str__(self):
        return "bonus is very high enter with in range"

class employee():
    def __init__(self):
        self.bonus = 2
        self.project = ["c","java","python"]

    def insert_details(self, emp_id, NameOfEmployee, Salary, Project):
        Search_id = ''' select emp_id from employee_table '''
        Format_for_search_id = Search_id.format(id)
        value_for_search_id = cursor.execute(Format_for_search_id)
        f = False
        for i in value_for_search_id:
            if i.emp_id == id:
                f = True
                break
        if f:
            try:
                raise Id_Error
            except Id_Error as id_ex:
                print(id_ex)
        else:
            query = ''' INSERT INTO employee_table (emp_id,NameOfEmployee,Salary,Project) values ({0},'{1}',{2},'{3}') '''
            insertquery = query.format(emp_id, NameOfEmployee, Salary, Project)
            if Project in self.project:
                cursor.execute(insertquery)
                cnxn.commit()
                print("details insert sucsessfully in db")
            else:
                try:
                    raise Insert_Error
                except Insert_Error as ex:
                    print(ex)

    def update_details(self,emp_id,Project='',Salary=0):
        if Salary !=0:
            query_for_salary_update= ''' UPDATE employee_table SET Salary = {0} where emp_id = {1} '''
            insertquery_for_salary_update=query_for_salary_update.format(Salary,emp_id)
            cursor.execute(insertquery_for_salary_update)
            cnxn.commit()
            print("updated sucssesfully")
        if Project:
            query_for_project= ''' UPDATE employee_table SET Project = '{0}' where emp_id = {1} '''
            insertquery_for_project_update = query_for_project.format(Project,emp_id)
            cursor.execute(insertquery_for_project_update)
            cnxn.commit()
            print("update susccessfully")
    def display_employee_details(self):
        query_for_display_details='''select * from employee_table '''
        values=cursor.execute(query_for_display_details)
        for i in values:
            print("employee id ",i.emp_id," employee name ",i.NameOfEmployee," salary ",i.Salary," project ",i.Project)
    def delete_employee_details(self,emp_id):
        query=''' DELETE from employee_table where emp_id = {0} '''.format(emp_id)
        cursor.execute(query)
        cnxn.commit()
        print("deleted sucsessfully")
    def add_bonus(self,id,bonus):
        if bonus > 0 and bonus <= 2:
            query = ''' select Salary from employee_table where emp_id = {}'''.format(id)
            value = cursor.execute(query)
            for i in value:
                Salary = i.Salary
            bonus_and_bonus = int(Salary + (Salary * bonus))
            query_for_update_bonus = ''' UPDATE employee_table SET Salary = {0} where emp_id = {1} '''.format(
                bonus_and_bonus, id)
            cursor.execute(query_for_update_bonus)
            cnxn.commit()
            print("bonus updated sucessfully")
        else:
            try:
                raise bonus_ex
            except bonus_ex as ex:
                print(ex)
obj = employee()
obj.insert_details(1,'SRI',50000,'c')
obj.update_details(4,'c',70000)
obj.display_employee_details()
obj.delete_employee_details(1)
obj.add_bonus(3,2)