class Employees:
    salary_percentage = 0
    defult_salary = 20000
    data_Employees = {"name" : ["john", "Alice", "Bob"],
                    "age" : [30, 25, 35],
                    "department" : ["HR", "IT", "Finance"], 
                    "years_of_experience" : [5, 3, 10],
                    "salary" : [50000, 60000, 70000]}
    def __init__(self, name):
        self.name = name
        self.dataEmp = Employees.data_Employees
        self.is_check()

    def is_check(self):
        return self.name in self.dataEmp["name"]
    
    def get_index(self):
        if self.is_check():
            return self.dataEmp["name"].index(self.name)
        return None
    
    def salary_raise(self):
        idx = self.get_index()
        if idx is not None:
            if self.dataEmp["years_of_experience"][idx] > 5:
                cur_salayr = self.dataEmp["salary"][idx]
                new_sala = cur_salayr + (cur_salayr * 0.20)
                self.dataEmp["salary"][idx] = new_sala
                Employees.salary_percentage = new_sala
                
                print(f"Salary raised by 20%. New salary: {new_sala:.2f}")
            else:
                print(f"Employee {self.name} has 5 or less years of experience. No raise applied.")
        else:
            print(f"Employee {self.name} not found. Cannot apply salary raise.")
            
    def add_emp(self, name, age, department,years_of_experience = 1):
        self.dataEmp["name"].append(name)
        self.dataEmp["age"].append(age)
        self.dataEmp["department"].append(department)
        self.dataEmp["years_of_experience"].append(years_of_experience)
        self.dataEmp["salary"].append(Employees.defult_salary )

    def remov_emp(self, name_to_remove):
            # دالة الحذف بعد تصحيحها تماماً
            if name_to_remove in self.dataEmp["name"]:
                loc = self.dataEmp["name"].index(name_to_remove)
                
                # نحذف العنصر بناءً على رقم المؤشر (Index) من كل القوائم
                self.dataEmp["name"].pop(loc)
                self.dataEmp["age"].pop(loc)
                self.dataEmp["department"].pop(loc)
                self.dataEmp["years_of_experience"].pop(loc)
                self.dataEmp["salary"].pop(loc)
                
                print(f"Employee {name_to_remove} removed successfully.")
                return True
            else:
                print(f"Employee {name_to_remove} not found.")
                return False
            
    def show_emp(self):
            idx = self.get_index()
            if idx is not None:
                print("\n--- Employee Data ---")
                print(f"Name: {self.dataEmp['name'][idx]}")
                print(f"Age: {self.dataEmp['age'][idx]}")
                print(f"Department: {self.dataEmp['department'][idx]}")
                print(f"Salary: {self.dataEmp['salary'][idx]}")
                print(f"Salary: {self.dataEmp['years_of_experience'][idx]} Years")
                print(f"Salary raised by : ({Employees.salary_percentage}) 20%")
                print("---------------------\n")
            else:
                print(f"Employee {self.name} not found.")
# Example usage

use = Employees("Ahmed Alhilali")

use.add_emp("Ahmed Alhilali",22,"CS",5)
use.salary_raise()
use.show_emp()



mas = Employees("Alhilali")
mas.add_emp("Alhilali",53,"HR",6)
mas.salary_raise()

mas.show_emp()