class Car:
    def __init__(self, company, speed, color, year):
        self.company = company
        self.color = color
        self.speed = speed
        self.year = year

    def get_speed(self):
        print(self.speed)
    
    def get_color(self):
        print(self.color)
    
    def get_company(self):
        print(self.company)
    
    def get_year(self):
        print(self.year)
    
# inhiritance / turunan
# bisa menggunakan methods & var dari parentnya

class Truck(Car):
    def __init__(self, company, speed, color, year):
        self.company = company
        self.speed = speed
        self.color = color
        self.year = year
