from dataclasses import dataclass


@dataclass()
class Student:
    id: str
    name: str
    tel_num: str
    email: str

    def __str__(self):
        return f"{self.id} {self.name} {self.tel_num} {self.email}"
