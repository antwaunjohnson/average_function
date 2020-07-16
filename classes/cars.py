class Cars:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()


class ElectricCar(Cars):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)


my_chevy = ElectricCar('chevy', 'spark', 2020)
print(my_chevy.get_descriptive_name())