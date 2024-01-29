class Person():
    def __init__(self, first_name, last_name="", number="", notes=""):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.notes = notes
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_phone_number(self):
        return self.number
    
    def set_notes(self, notes):
        self.notes = notes
    
    