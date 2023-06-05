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

    @abstractmethod
    def get_attr_dict(self):
        pass

    @classmethod
    def get_file_path(cls):
        return csv_dirs / cls.filename

    def save(self):
        filepath = self.get_file_path()

        with open(filepath, mode="a+", newline="") as file:
            reader = csv.DictReader(file)
            file.seek(0)
            items = list(reader)

            writer = csv.DictWriter(file, fieldnames=self.fieldnames)

            if os.path.getsize(filepath) == 0:
                writer.writeheader()

            if not is_unique(self.id, items):
                raise ValueError(f"{self.__class__.__name__} with ID {self.id} already exists.")

            writer.writerow(self.get_attr_dict())

    @classmethod
    def remove(cls, _id):
        rows = []
        filepath = cls.get_file_path()
        with open(filepath, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if row[0] != _id:
                    rows.append(row)

        with open(filepath, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(rows)

    @classmethod
    def update(cls, _id, updated_fields):
        filepath = cls.get_file_path()
        updated_row = None

        with open(filepath, mode="r") as file:
            reader = csv.DictReader(file)
            items = list(reader)

            for item in items:
                if item['ID'] == _id:
                    updated_row = item
                    break

        if updated_row is None:
            raise ValueError(f"{cls.__name__} with ID {_id} does not exist.")

        updated_row.update(updated_fields)

        with open(filepath, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=cls.fieldnames)
            writer.writeheader()
            writer.writerows(items)

    @classmethod
    @abstractmethod
    def get_search_criteria(cls):
        return []

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

        filepath = cls.get_file_path()

        with open(filepath, mode="r") as file:
            reader = csv.DictReader(file)
            items = list(reader)

        instances = []

        for item in items:
            if all(item[key] == str(value) for key, value in criteria.items()):
                instances.append(cls(**item))

        return instances
