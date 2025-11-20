#--------INHERITANCE--------
class Vehicle:
    def __init__(self, brand, fuel):
        self.brand = brand
        self.fuel = fuel

class Car(Vehicle):
    def __init__(self, brand, fuel, doors):
        # Call the parent class constructor
        Vehicle.__init__(self, brand, fuel)
        self.doors = doors

    def drive(self):
        if self.fuel > 0:
            self.fuel -= 1
            print(f"The {self.brand} car is driving... Fuel left: {self.fuel}")
        else:
            print(f"The {self.brand} car has no fuel left!")

# Example usage:
my_car = Car("Toyota", 5, 4)
my_car.drive()
my_car.drive()
my_car.drive()


#--------ENCAPSULATION--------
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance= balance
        
    def deposit(self, amount):
        self.balance += amount
        print (f"{self.owner} deposited Php {amount}. New balance: Php{self.balance}")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew Php{amount}. Remaining balance: Php {self.balance}")
        else:
            print("Insuficient funds!")

amount1= BankAccount("Jv", 1500)
amount1.deposit(1500)
amount1.withdraw(3000)
amount1.withdraw(10000)


#--------ABSTRACTION--------
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_pay(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, rate, hours):
        self.rate = rate
        self.hours = hours

    def calculate_pay(self):
        return self.rate * self.hours

class SalariedEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_pay(self):
        return self.salary

h_emp = HourlyEmployee(100, 8)
s_emp = SalariedEmployee(30000)

print("Hourly Employee Pay:", h_emp.calculate_pay())
print("Salaried Employee Pay:", s_emp.calculate_pay())


#--------POLYMORPHISM--------
class InkPrinter:
    def print_document(self):
        return "Printing using ink..."

class LaserPrinter:
    def print_document(self):
        return "Printing using laser..."

printers = [InkPrinter(), LaserPrinter()]
for p in printers:
    print(p.print_document())

#-----Part 2

def make_it_speak(obj):
    obj.speak()

class Bird:
    def speak(self):
        print("Tweett tweett!")

class Robot:
    def speak(self):
        print("Beepp boop!")

make_it_speak(Bird())
make_it_speak(Robot())
