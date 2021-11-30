class Employee():

    def __init__(self, first_name, last_name, salary, middle_name = None):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = 40000
        self.middle_name = middle_name

    def full_name(self):
        if self.middle_name is not None:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.last_name}"

    def set_salary(self, new_salary):
        try:
            self.salary = int(new_salary)
            if self.salaray < 40000:
                self.salary = 40000
        except:
            pass


new_employee_1 = Employee("Mark", "Adams", "Anthony")
new_employee_2 = Employee("Blue", "Alas", "Any")
new_employee_3 = Employee("Kidd", "Arams", "Anty")
new_employee_4 = Employee("Mang", "Mony")

employees = [new_employee_1, new_employee_2, new_employee_3, new_employee_4]

#for employee in Employees
# employee.set_salary(employee.salary *1.1)

new_employee_1.set_salary(60000)
new_employee_2.set_salary(new_employee_2 * 1.05)
new_employee_4.set_salary("72000")
new_employee_4.set_salary("fifty five thousand, two hundred and nine dollars") #not capable

for employee in employees:
    print(employee.salary)
    print(type(employee.salary))
