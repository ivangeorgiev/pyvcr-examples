import dataclasses

@dataclasses.dataclass
class Person:
    name: str
    height: int
    mass: int
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str


    def asdict(self):
        return dataclasses.asdict(self)
