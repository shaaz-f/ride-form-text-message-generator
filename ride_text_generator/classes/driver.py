from .person import Person

class Driver(Person):
    def __init__(self, first_name, last_name, number, drivernotes=""):
        self.riders = []
        super().__init__(first_name, last_name, number, notes=drivernotes)

    def get_riders(self):
        return self.riders

    def add_rider(self, rider):
        self.riders.append(rider)

