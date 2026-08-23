from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self._name = name
        self._type = creature_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self._name} is a {self._type} type Creature"


class Flameling(Creature):
    def attack(self) -> str:
        return f"{self._name.capitalize()} uses Ember!"


class Pyrodon(Creature):
    def attack(self) -> str:
        return f"{self._name.capitalize()} uses Flamethrower!"


class Aquabub(Creature):
    def attack(self) -> str:
        return f"{self._name.capitalize()} uses Water Gun!"


class Torragon(Creature):
    def attack(self) -> str:
        return f"{self._name.capitalize()} uses Hydro Pump!"
