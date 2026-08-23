from ex0.creatures import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self._name.capitalize()} uses Vine Whip!"

    def heal(self, target: Creature) -> str:
        if self == target:
            return f"{self._name} heals itself for a small amount"
        else:
            return f"{self._name} heals '{str(target)}' for a small amount"


class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self._name.capitalize()} uses Petal Dance!"

    def heal(self, target: Creature | None = None) -> str:
        if not target or target == self:
            return f"{self._name} heals itself for a large amount"
        else:
            return (
                f"{self._name} heals itself and '{str(target)}' "
                "for a large amount"
            )


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, creature_type: str):
        super().__init__(name, creature_type)
        self.is_transformed = False

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self._name.capitalize()} performs a boosted strike!"
        return f"{self._name.capitalize()} attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self._name.capitalize()} shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self._name.capitalize()} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, creature_type: str):
        super().__init__(name, creature_type)
        self.is_transformed = False

    def attack(self) -> str:
        if self.is_transformed:
            return (
                f"{self._name.capitalize()} "
                "unleashes a devastating morph strike!"
            )
        return f"{self._name.capitalize()} attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self._name.capitalize()} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self._name.capitalize()} stabilizes its form."
