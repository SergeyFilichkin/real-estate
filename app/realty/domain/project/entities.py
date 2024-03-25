from dataclasses import dataclass


@dataclass
class BuildingsEntity:
    name: str
    floors: int
    date_of_construction: str
    date_of_delivery: str
    address: str
    number: int
    status: str
    type: str
    has_parking: bool
    elevators: int
    project: str
    total_flats: int


@dataclass
class ProjectEntity:
    id: int
    name: str
    description: str
    buildings: list[BuildingsEntity]
