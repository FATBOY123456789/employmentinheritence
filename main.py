class Person:
    def __init__(self,name,idno):
        self.name=name
        self.idno=idno
    def display(self):
        print('He is ',self.name,'his id no. is',self.idno)
class Employee(Person):
    def __init__(self, name, idno,salary,post):
        self.name=name
        self.idno=idno
        self.salary=salary
        self.post=post
    def display(self):
        super().display()
        print('His salary is ',self.salary,'and his post is ',self.post)
a=Employee('Rahul',880521,220000,'intel')
a.display()