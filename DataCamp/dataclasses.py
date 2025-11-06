@dataclass
class WeightEntry:
    # Define the fields on the class
    species: str
    flipper_length: int
    body_mass: int
    sex: str

    @property
    def mass_to_flipper_length_ratio(self):
        return self.body_mass / self.flipper_length
