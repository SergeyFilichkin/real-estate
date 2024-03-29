from dataclasses import dataclass

from realty.domain.building.entities import DetailBuildingEntity


@dataclass
class ProjectEntity:
    id: int
    name: str
    description: str
    buildings: list[DetailBuildingEntity]
