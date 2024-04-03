from dataclasses import dataclass

from realty.domain.building.entities import BuildingEntity


@dataclass
class ProjectEntity:
    id: int
    name: str
    description: str
    buildings: list[BuildingEntity]
