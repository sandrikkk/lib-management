import csv
import os
import uuid
from abc import ABC, abstractmethod
from settings import csv_dirs
from utils import is_unique


# makefile
class BaseModel(ABC):
    filename = ""
    fieldnames = []

    def __init__(self, id=None):  # noqa
        if id:
            self.id = id
        else:
            self.id = str(uuid.uuid4())

    @classmethod
    def read_csv(cls):
        filepath = cls.get_file_path()

        with open(filepath, mode="r") as file:
            reader = csv.DictReader(file)
            items = list(reader)

        return items

    @classmethod
    def write_csv(cls, items: list[dict]):
        filepath = cls.get_file_path()

        with open(filepath, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=cls.fieldnames)

            if os.path.getsize(filepath) == 0:
                writer.writeheader()

            writer.writerows(items)

    @abstractmethod
    def get_attr_dict(self):
        pass

    @classmethod
    def get_file_path(cls):
        return csv_dirs / cls.filename

    @classmethod
    @abstractmethod
    def get_search_criteria(cls):
        return []

    def save(self):
        filepath = self.get_file_path()

        with open(filepath, mode="a+", newline="") as file:
            reader = csv.DictReader(file)
            file.seek(0)
            items = list(reader)

            if not is_unique(self.id, items):
                raise ValueError(f"{self.__class__.__name__} with ID {self.id} already exists.")

            writer = csv.DictWriter(file, fieldnames=self.fieldnames)

            if os.path.getsize(filepath) == 0:
                writer.writeheader()

            writer.writerow(self.get_attr_dict())

    @classmethod
    def remove(cls, _id):
        rows = []

        items = cls.read_csv()
        for row in items:
            if row["id"] != _id:
                rows.append(row)

        cls.write_csv(rows)

    @classmethod
    def update(cls, _id, updated_fields):
        updated_row = None

        items = cls.read_csv()

        for item in items:
            if item['id'] == _id:
                updated_row = item
                break

        if updated_row is None:
            raise ValueError(f"{cls.__name__} with ID {_id} does not exist.")

        updated_row.update(updated_fields)

        cls.write_csv(items)

    @classmethod
    def validate_search_fields(cls, criteria: dict):
        error_list = []
        for key, value in criteria.items():
            if key not in cls.get_search_criteria():
                error_list.append(key)

        if error_list:
            raise ValueError(f"Wrong search criteria(s): {', '.join(error_list)}")

    @classmethod
    def search(cls, criteria: dict):
        cls.validate_search_fields(criteria)

        items = cls.read_csv()

        instances = []

        for item in items:
            if all(item[key] == str(value) for key, value in criteria.items()):
                instances.append(cls(**item))

        return instances
