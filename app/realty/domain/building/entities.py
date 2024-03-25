from dataclasses import dataclass


@dataclass
class BuildingEntity:
    id: int
    floors: int
    name: str
    date_of_construction: str
    date_of_delivery: str
    address: str
    number: int
    status: str
    type: str
    has_parking: bool
    elevators: int
    total_flats: int
