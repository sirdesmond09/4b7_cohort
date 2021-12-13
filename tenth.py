from datetime import datetime


class Employee():
    
    company = "OK-HI"
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __str__(self):
        return f'{self.name} {self.age} {self.salary}'
    
    
    def __add__(self, other):
        if isinstance(other, Employee):
            
            return self.salary + other.salary
        
        raise TypeError(f"Expected type {type(self)} but got {type(other)}")


    def __get_yob(self):
        """This is a private method that calculates the year of birth.

        Returns:
            [int]: [year of birth]
        """
        
        year = datetime.now().year
        return year - self.age
    
    
    def bonus(self):
        """This function calculates the bonus of an employee if the age is greater or equal to a threshold age.

        Returns:
            [int]: [10 percent of the employee's salary]
        """
        bonus_age = 30
        if self.age >= bonus_age:
            bonus_amount = self.salary * 0.1
            
            return bonus_amount
        
        else:
            return 0
        
        
    def child_support(self):
        if self.__get_yob()  <= 1990:
            return 2500
        
        else:
            return 0
            
    
    @property
    def take_home_salary(self):
        return self.salary + self.bonus() + self.child_support()
    
    

employee1 = Employee("John Doe", 32, 32000)
employee2 = Employee("Jane Doe", 29, 30000)
# employee3 = Employee("Me", 3, 3333)

# print(employee1)
# print(employee1. child_support())
# print(employee2.child_support())

# print(employee1 + employee2)

print(employee1.take_home_salary)




class EngineeringTeam(Employee):
    
    def __init__(self, name, age, salary, track):
        self.track = track
        super().__init__(name, age, salary)
        
        
        
    
        
        
engieering1 = EngineeringTeam("Desmond", 12, 2000000, "Fullstack")
engieering2 = EngineeringTeam("Jack", 15, 2000030, "Backend")

print(engieering1 + engieering2)