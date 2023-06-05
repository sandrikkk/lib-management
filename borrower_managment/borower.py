from base.base import BaseModel


class Borrower(BaseModel):
    filename = "borrowers.csv"
    fieldnames = ["id", "name", "last_name", "phone", "address", "personal_number"]

    def __init__(self, name, last_name, phone, address, personal_number, id=None):
        super().__init__(id)
        self.name = name
        self.last_name = last_name
        self.personal_number = personal_number
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f"UUID: {self.id}, Borrower-{self.name} {self.last_name}, {self.personal_number}"

    def get_attr_dict(self):
        attrs = {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "phone": self.phone,
            "address": self.address,
            "personal_number": self.personal_number
        }

        return attrs

    @classmethod
    def get_search_criteria(cls):
        return ["name", "last_name", "phone", "address", "personal_number"]
