class Employee:
    def __init__(self, name:str, position:str) -> None:
        self.name = name 
        self.position = position
        
    # INSTANCE METHOD
    def get_details(self) -> str:
        return f"{self.name} {self.position}"
    
    # STATIC METHOD
    @staticmethod
    def is_valid_position(position:str) -> bool:
        valid_positions = ["SWE", "Backend", "Mobile", "Frontend"]
        return position in valid_positions
    
    
emp1 = Employee("Zeyad", "Backend")    
emp2 = Employee("Mohammed", "Frontend")    
emp3 = Employee("Abdo", "Mobile")    
  
print(emp1.get_details()) 
print(emp2.get_details()) 
print(emp3.get_details()) 
  
    
Employee.is_valid_position("SWE")


Employee.is_valid_position("DevOps")
    
    
