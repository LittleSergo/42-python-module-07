from ex0 import CreatureFactory
from . import creatures


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> creatures.Sproutling:
        return creatures.Sproutling("Sproutling", "Grass")

    def create_evolved(self) -> creatures.Bloomelle:
        return creatures.Bloomelle("Bloomelle", "Grass/Fairy")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> creatures.Shiftling:
        return creatures.Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> creatures.Morphagon:
        return creatures.Morphagon("Morphagon", "Normal/Dragon")
