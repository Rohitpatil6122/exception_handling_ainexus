class Employee_bonus_gross:
    def __init__(self,id,name,city,salary,bonus):
        self.id=id
        self.name=name
        self.city=city
        self.salary=salary
        self.bonus=bonus
    def cal_gross_sal(self):
        gross_sal=self.salary+self.bonus
        return gross_sal
    def show_emp_details(self):
        print("id: ",self.id)
        print("name: ",self.name)
        print("city: ",self.city)
        print("salery: ",self.salary)
        print("gross",gross)
obj=Employee_bonus_gross(101,"rohit","kolhapur",50000,20000)
gross=obj.cal_gross_sal()
obj.show_emp_details()



