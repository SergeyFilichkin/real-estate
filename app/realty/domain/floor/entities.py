from dataclasses import dataclass


@dataclass
class FlatsEntity:
    square: int
    living_space: int
    kitchen_area: int
    rooms: int
    status: str
    price: int
    description: str
    photo: str
    floor: int
    category: str
    building: int


@dataclass
class FloorEntity:
    id: int
    name: str
    number: int
    flats: list[FlatsEntity]
