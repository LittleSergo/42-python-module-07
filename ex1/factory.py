from ex0 import CreatureFactory
from ex0.creatures import Creature
from . import creatures


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return creatures.Sproutling("Sproutling", "Grass")

    def create_evolved(self) -> Creature:
        return creatures.Bloomelle("Bloomelle", "Grass/Fairy")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return creatures.Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> Creature:
        return creatures.Morphagon("Morphagon", "Normal/Dragon")
