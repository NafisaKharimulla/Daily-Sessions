from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary, allowance, tax):
        super().__init__(name)
        self.base_salary = base_salary
        self.allowance = allowance
        self.tax = tax

    def calculate_salary(self):
        return self.base_salary + self.allowance - self.tax


class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class PayrollSystem:
    def __init__(self):
        self.employees = []   # list lives here

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_payroll(self):
        total = 0
        print("Employee Payroll\n")

        for emp in self.employees:
            salary = emp.calculate_salary()   # polymorphism
            print(f"{emp.name} earns: {salary}")
            total += salary

        print("\nTotal Payroll Amount:", total)

def main():
    payroll = PayrollSystem()

    # Adding employees to the list
    payroll.add_employee(FullTimeEmployee("Emp1", 50000, 10000, 8000))
    payroll.add_employee(ContractEmployee("Emp2", 500, 80))

    payroll.calculate_total_payroll()


if __name__ == "__main__":
    main()
