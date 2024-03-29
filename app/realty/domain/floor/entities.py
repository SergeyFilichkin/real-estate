from dataclasses import dataclass

from realty.domain.flat.entities import DetailFlatEntity


@dataclass
class FloorEntity:
    id: int
    name: str
    number: int
    flats: list[DetailFlatEntity]
