# first_employee = {
#     "first_name" : "Mike",
#     "last_name" : "Lawson",
#     "salary" : 78000
# }
# second_employee = {
#     "first_name" : "Sarah",
#     "last_name" : "Michaels",
#     "salary" : 98000
# }
# third_employee ={
#     "first_name" : "",
#     "last_name" : "Lawson",
#     "salary" : 53000
# }

# employees = [first_employee, second_employee, third_employee]

# for employee in employees:
#     employee["salary"] *=1.1
#     print(employee["salary"])

class Employee():
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def full_name(self):
        return f"{self.first_name}{self.last_name}"

new_employee = Employee("mark", "adams", 80000)

new_employee1 = Employee("Mark", "Adams", 80000)
new_employee2 = Employee("Justin", "Adams", 90000)
new_employee3 = Employee("Angel", "Adams", 88000)

employees = [new_employee1, new_employee2, new_employee3]

for employee in employees: 
    # print(f"{first_name}{last_name}")
    print(f"{employee.full_name()}")