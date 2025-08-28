from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Product:
    id: str
    name: str
    description: str
    price: float
    created_at: datetime
    updated_at: datetime

    def validate(self):
        if not self.name:
            raise ValueError("Name is required")
        if self.price is None:
            raise ValueError("Price is required")
        if not isinstance(self.price, int):
            raise ValueError("Price must be an integer")
        if self.price < 0:
            raise ValueError("Price must be positive")