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

    # @classmethod
    # def borrower_list(cls):
    #     print("Book list was accessed !")
    #     if cls.borrowers_users:
    #         for borrower in cls.borrowers_users:
    #             print(f"Name: {borrower.name},"
    #                   f"Last Name: {borrower.last_name}"
    #                   f"Personal Number: {borrower.personal_number}"
    #                   )
    #     return cls.borrowers_users
    #
    #
    # @classmethod
    # def search_borrowers(cls, borrower_search_field, borrower_field_value):
    #     search_list_borrowers = []
    #
    #     for borrower in cls.borrowers_users:
    #         if borrower_search_field == 'personal_number' and borrower_field_value == borrower.personal_number:
    #             search_list_borrowers.append(borrower)
    #
    #     if search_list_borrowers:
    #         return search_list_borrowers
    #     else:
    #         return "Not found any book borrowers or parameters are invalid!"
