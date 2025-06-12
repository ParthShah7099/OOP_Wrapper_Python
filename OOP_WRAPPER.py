"""
PR.5 OOP WRAPPER

The goal of this project is to build an Employee management System that utilizez various
Object-Oriented Programming (OOP) concepts like classes, inheritance, encapsulation, method
overloading, method overriding, and more. The system will model employee data and operations
related to adding, updating, and removing employees as well as tracking their roles (eg.,
Manager, Developer).

"""

class Employee:
    """
    Base class for all employee types.
    Implements encapsulation with private attributes and getter/setter methods.

    """
    
    def __init__(self, name=None, age=None, employee_id=None, salary=None):
        """
        Constructor with method overloading (multiple ways to create objects)
        Can be called with no arguments, or with all arguments

        """
        self._name = name
        self._age = age
        self._employee_id = employee_id  
        self._salary = salary            
    
    def __del__(self):
        print(f"Employee {self._name} record deleted.")
    
    def get_salary(self):
        return self._salary
    
    def set_salary(self, salary):
        if salary >= 0: 
            self._salary = salary
        else:
            print("Salary cannot be negative.")
    
    def get_employee_id(self):
        return self._employee_id
    
    def set_employee_id(self, employee_id):
        if employee_id:  
            self._employee_id = employee_id
        else:
            print("Employee ID cannot be empty.")
    
    def display(self):
        print("Employee Details:")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Employee ID: {self._employee_id}")
        print(f"Salary: ${self._salary}")
    
    def __str__(self):
        return f"Employee: {self._name} (ID: {self._employee_id})"
    
    def __eq__(self, other):
        return self._salary == other._salary
    
    def __lt__(self, other):
        return self._salary < other._salary
    
    def __gt__(self, other):
        return self._salary > other._salary


class Manager(Employee):
    """
    Derived class from Employee for Manager type.
    Demonstrates inheritance and method overriding.

    """
    
    def __init__(self, name=None, age=None, employee_id=None, salary=None, department=None):
        super().__init__(name, age, employee_id, salary)  
        self.department = department
    
    def display(self):
        print("Manager Details:")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Employee ID: {self._employee_id}")
        print(f"Salary: ${self._salary}")
        print(f"Department: {self.department}")
    
    def __str__(self):
        return f"Manager: {self._name} (Department: {self.department})"


class Developer(Employee):
    """
    Derived class from Employee for Developer type.
    Demonstrates inheritance and method overriding.

    """
    
    def __init__(self, name=None, age=None, employee_id=None, salary=None, programming_language=None):
        super().__init__(name, age, employee_id, salary)  
        self.programming_language = programming_language
    
    def display(self):
        print("Developer Details:")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Employee ID: {self._employee_id}")
        print(f"Salary: ${self._salary}")
        print(f"Programming Language: {self.programming_language}")
    
    def __str__(self):
        return f"Developer: {self._name} (Language: {self.programming_language})"

employees = {}


def create_person():
    """ Function to create a basic person (not an employee) """
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    print(f"\nPerson created with name: {name} and age: {age}.\n")


def create_employee():
    """ Function to create an Employee object """
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    employee_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    
    emp = Employee(name, age, employee_id, salary)
    employees[employee_id] = emp
    print(f"\nEmployee created with name: {name}, age: {age}, ID: {employee_id}, and salary: ${salary}.\n")


def create_manager():
    """ Function to create a Manager object """
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    employee_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")
    
    mgr = Manager(name, age, employee_id, salary, department)
    employees[employee_id] = mgr
    print(f"\nManager created with name: {name}, age: {age}, ID: {employee_id}, salary: ${salary}, and department: {department}.\n")


def show_details():
    """ Function to display details of created objects """
    print("\nChoose details to show:")
    print("1. Person (Not available - persons are not stored)")
    print("2. Employee")
    print("3. Manager")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("\nPerson details not stored in this system.\n")
    elif choice == "2":
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees and isinstance(employees[emp_id], Employee) and not isinstance(employees[emp_id], (Manager, Developer)):
            employees[emp_id].display()
        else:
            print("\nEmployee not found or not a basic Employee.\n")
    elif choice == "3":
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees and isinstance(employees[emp_id], Manager):
            employees[emp_id].display()
        else:
            print("\nManager not found or ID does not belong to a Manager.\n")
    else:
        print("\nInvalid choice.\n")


def compare_salaries():
    """ Function to compare salaries of two employees """
    print("\nChoose two employees to compare salaries.")
    id1 = input("Enter the first employee's ID (e.g., E123): ")
    id2 = input("Enter the second employee's ID (e.g., M456): ")
    
    if id1 in employees and id2 in employees:
        emp1 = employees[id1]
        emp2 = employees[id2]
        
        print("\nComparing salaries:")
        if emp1 > emp2:
            print(f"Employee {emp1._name} ({id1}) has a higher salary than {type(emp2).__name__} {emp2._name} ({id2}).")
        elif emp1 < emp2:
            print(f"Employee {emp1._name} ({id1}) has a lower salary than {type(emp2).__name__} {emp2._name} ({id2}).")
        else:
            print(f"Employee {emp1._name} ({id1}) has the same salary as {type(emp2).__name__} {emp2._name} ({id2}).")
    else:
        print("\nOne or both employee IDs not found.\n")


def main_menu():
    """ Main menu function for the user interface """
    while True:
        print("\n--- Python OOP Project: Employee Management System ---")
        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Compare Salaries")
        print("6. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            create_person()
        elif choice == "2":
            create_employee()
        elif choice == "3":
            create_manager()
        elif choice == "4":
            show_details()
        elif choice == "5":
            compare_salaries()
        elif choice == "6":
            print("\nExiting the system. All resources have been freed.")
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
