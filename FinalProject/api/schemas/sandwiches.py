from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SandwichBase(BaseModel):
    name: str
    calories: Optional[float] = None
    price: Optional[float] = None
    category: Optional[str] = None


class SandwichCreate(SandwichBase):
    pass


class SandwichUpdate(SandwichBase):
    sandwich_name: Optional[str] = None
    price: Optional[float] = None


class Sandwich(SandwichBase):
    id: int

    class ConfigDict:
        from_attributes = True