from dataclasses import dataclass
# In Python, a data class is a class that is designed to only hold data values.
# They aren't different from regular classes, but they usually don't have
# any other methods. They are typically used to store information that will be
# passed between different parts of a program or a system

@dataclass()
class Product:
    id: str
    parent:str
    title:str
    category: str

    def __str__(self):
        return f"{self.id} {self.title} {self.category}"