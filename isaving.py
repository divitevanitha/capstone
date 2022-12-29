query=('''create table Employee_informat(
EMP_ID int NOT NULL, 
NAME varchar(30),
SALARY int,
PROJECT varchar(30)
PRIMARY KEY(EMP_ID))''')
cursor.execute(query)
cnxn.commit()

if self.project in self.projects:
    self.insert_Employee_details()
else:
    print("Unable insert data due to incorrect project name")

    def __init__(self,emp_id,name,salary,project):
        self.emp_id = emp_id
        self.name=name
        self.salary=salary
        self.project=project