#!/usr/bin/env python3

from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()
    print(base_creature, base_creature.attack(), sep="\n")
    print(evolved_creature, evolved_creature.attack(), sep="\n")


def fight(factory_1: CreatureFactory, factory_2: CreatureFactory) -> None:
    opponent_1 = factory_1.create_base()
    opponent_2 = factory_2.create_base()
    print(f"{opponent_1}\n vs.\n{opponent_2}\n fight!")
    print(opponent_1.attack(), opponent_2.attack(), sep="\n")


if __name__ == "__main__":
    aqua = AquaFactory()
    flame = FlameFactory()
    test_factory(aqua)
    print()
    test_factory(flame)
    print()
    fight(flame, aqua)
