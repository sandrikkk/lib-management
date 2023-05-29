class Borrower:
    def __init__(self, name, last_name, phone, address, personal_number):
        self.name = name
        self.last_name = last_name
        self.personal_number = personal_number
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f"Borrower-{self.name} {self.last_name}, {self.personal_number}"

