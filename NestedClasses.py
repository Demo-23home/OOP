

class Company:
    def __init__(self, company_name:str) -> None:
        self.company_name = company_name
        self.employees = []
        
    class Employee:
        def __init__(self, name:str, position:str) -> None:
            self.name = name
            self.position = position
            
        def get_details(self) -> str:
            return f"{self.name} working as {self.position}"
    
        
    def add_employee(self, name:str, position:str) -> None:
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)
        
        
    def list_employee(self) -> list[str]:
        return [emp.get_details() for emp in self.employees]
    


company = Company("NewCompany")
company.add_employee("Zeyad", "SWE")
company.add_employee("Mohammed", "Backend")
company.add_employee("Salama", "Mobile")
emps = company.list_employee()
for emp in emps:
    print(emp)