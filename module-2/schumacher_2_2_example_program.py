# calebSchumacher_11162025_Module10
# Display employee information in a readable format


class Employee:
    def __init__(self, name, gender, rate, number):
        self.name = name
        self.gender = gender
        self.rate = rate
        self.number = number

    def set_name(self, name): # Setters
        self.name = name

    def set_gender(self, gender):
        self.gender = gender

    def set_rate(self, rate):
        self.rate = rate

    def set_number(self, number):
        self.number = number

    def display_info(self): # Getter
        print(f"Name: {self.name}, Gender: {self.gender}, Rate: {self.rate}, Employee Number: {self.number}")
    
class ProductionWorker(Employee):
    def __init__(self, name, gender, rate, number, shift):
        super().__init__(name, gender, rate, number)
        self.set_shift(shift)

    def set_shift(self, shift): # Setter
        if shift in [1, 2, 3]:
            self.shift = shift 
        else:
            self.shift = 1 # Default shift is 1

    def display_info(self): # Getter
        print(f"Name: {self.name}, Gender: {self.gender}, Rate: {self.rate}, Employee Number:  {self.number}, Shift: {self.shift}")






def main():
    
    employee1 = ProductionWorker("Samuel", "Male", 25, 12345, 1)

    employee2 = ProductionWorker("Jerry", "Male", 27, 12346, 2)

    employee3 = Employee("Sarah", "Female", 26, 13247)
    
    employee4 = Employee("Sandra", "Female", 25, 12348)

    print("== Employee Information ==")
    employee1.display_info()
    employee2.display_info()
    employee3.display_info()
    employee4.display_info()









if __name__ == "__main__":
    main()