#!/usr/bin/env python3
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory


def capacitor() -> None:
    healFact = HealingCreatureFactory()
    transFact = TransformCreatureFactory()
    sprout = healFact.create_base()
    bloom = healFact.create_evolved()
    shift = transFact.create_base()
    morph = transFact.create_evolved()

    print("Testing Creature with healing capability")

    print("base:")
    print(sprout.describe())
    print(sprout.attack())
    print(sprout.heal("itself"))

    print("evolved:")
    print(bloom.describe())
    print(bloom.attack())
    print(bloom.heal("itself and others"))

    print("\nTesting Creature with transform capability")

    print("base:")
    print(shift.describe())
    print(shift.attack())
    print(shift.transform())
    print(shift.attack())
    print(shift.revert())

    print("evolved:")
    print(morph.describe())
    print(morph.attack())
    print(morph.transform())
    print(morph.attack())
    print(morph.revert())


if __name__ == "__main__":
    capacitor()
