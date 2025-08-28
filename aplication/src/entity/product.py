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
        if self.price <= 0:
            raise ValueError("Price must be positive")