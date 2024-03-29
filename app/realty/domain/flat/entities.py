from dataclasses import dataclass


@dataclass
class DetailFlatEntity:
    id: int
    square: float
    living_space: float
    kitchen_area: float
    rooms: int
    status: str
    price: int
    description: str
    photo: str
    floor: int
    category: int
    building: int


@dataclass
class ListFlatEntity:
    all_flats: list[DetailFlatEntity]
