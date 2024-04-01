from dataclasses import dataclass


@dataclass
class FlatEntity:
    id: int
    square: float
    living_space: float
    kitchen_area: float
    rooms: int
    status: str
    price: int
    description: str
    photo: str
    floor_number: int
    category_name: str
    building_name: str
