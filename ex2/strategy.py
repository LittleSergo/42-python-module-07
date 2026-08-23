from abc import ABC, abstractmethod

from ex0.creatures import Creature
from ex1.capabilities import TransformCapability, HealCapability


class InvalidStrategyError(Exception):
    def __init__(self, message: str = "Invalid Creature for this strategy"):
        super().__init__(message)


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
            return None
        raise InvalidStrategyError(
            f"This creature '{creature}' doesn't support Normal strategy!"
        )

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(
                f"{creature.transform()}\n{creature.attack()}\n"
                f"{creature.revert()}"
            )
            return None
        raise InvalidStrategyError(
            f"This creature '{creature}' doesn't support Aggressive strategy!"
        )

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(f"{creature.attack()}\n{creature.heal(creature)}")
            return None
        raise InvalidStrategyError(
            f"This creature '{creature}' doesn't support Defensive strategy!"
        )

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
