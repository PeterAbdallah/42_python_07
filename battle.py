#!/usr/bin/env python3

from ex0 import factories as f


def test_factories() -> None:
    flame = f.FlameFactory()
    aqua = f.AquaFactory()

    flameling = flame.create_base()
    pyrodon = flame.create_evolved()

    aquabub = aqua.create_base()
    torragon = aqua.create_evolved()

    print("Testing factory")
    print(flameling.describe())
    print(flameling.attack())
    print(pyrodon.describe())
    print(pyrodon.attack())

    print("\nTesting factory")
    print(aquabub.describe())
    print(aquabub.attack())
    print(torragon.describe())
    print(torragon.attack())


def battle() -> None:
    flame = f.FlameFactory()
    flameling = flame.create_base()
    aqua = f.AquaFactory()
    aquabub = aqua.create_base()

    print("\nTesting battle")
    print(flameling.describe())
    print("vs.")
    print(aquabub.describe())
    print("fight!")
    print(flameling.attack())
    print(aquabub.attack())


if __name__ == "__main__":
    test_factories()
    battle()
