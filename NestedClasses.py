

class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []
        
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position
            
        def get_details(self):
            return f"{self.name} working as {self.position}"
    
        
    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)
        
        
    def list_employee(self):
        return [emp.get_details() for emp in self.employees]
    


company = Company("NewCompany")
company.add_employee("Zeyad", "SWE")
company.add_employee("Zeyad", "SWE")
company.add_employee("Zeyad", "SWE")
emps = company.list_employee()
print(*emps)