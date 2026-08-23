#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_heal_factory(factory: HealingCreatureFactory) -> None:
    print("Testing Creatures with healing capabilities")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(f" base:\n{base}\n{base.attack()}\n{base.heal(base)}")
    print(f" evolved:\n{evolved}\n{evolved.attack()}\n{evolved.heal(evolved)}")


def test_transform_factory(factory: TransformCreatureFactory) -> None:
    print("Testing Creatures with transform capabilities")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(
        f" base:\n{base}\n{base.attack()}\n"
        f"{base.transform()}\n{base.attack()}\n{base.revert()}"
    )
    print(
        f" evolved:\n{evolved}\n{evolved.attack()}\n"
        f"{evolved.transform()}\n{evolved.attack()}\n{evolved.revert()}"
    )


if __name__ == "__main__":
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    test_heal_factory(heal_factory)
    print()
    test_transform_factory(transform_factory)
