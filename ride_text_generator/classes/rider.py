from .person import Person

class Rider(Person):
    def __init__(self, first_name, last_name="", number="", address="", driver=None, ridernotes=""):
        self.driver = driver
        self.address = address
        super().__init__(first_name, last_name, number, notes=ridernotes)

    def get_driver(self):
        return self.driver
    
    def get_address(self):
        return self.address
    
    def set_driver(self, driver):
        self.driver = driver