#!/usr/bin/env python3

from ex0.factories import FlameFactory, AquaFactory
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategies import (NormalStrategy,
                            AggressiveStrategy,
                            DefensiveStrategy)


def run_battle(c1, s1, c2, s2) -> None:
    print("* Battle *")
    print(c1.describe())
    print("vs.")
    print(c2.describe())
    print("now fight!")

    # first creature
    print(s1.act(c1))

    # second creature (with error handling for aggressive case)
    try:
        print(s2.act(c2))
    except Exception as e:
        raise e


def tournament(name: str, opponents):
    print(f"Tournament {name}")
    print(opponents)
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    creatures = []

    # create creatures
    for factory, strategy in opponents:
        base = factory.create_base()
        creatures.append((base, strategy))

    # all vs all (simple round-robin)
    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):
            c1, s1 = creatures[i]
            c2, s2 = creatures[j]

            try:
                run_battle(c1, s1, c2, s2)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main():
    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    trans = TransformCreatureFactory()

    # Tournament 0
    tournament("0 (basic)", [
        (flame, NormalStrategy()),
        (heal, DefensiveStrategy()),
    ])

    print()

    # Tournament 1
    tournament("1 (error)", [
        (flame, AggressiveStrategy()),
        (heal, DefensiveStrategy()),
    ])

    print()

    # Tournament 2
    tournament("2 (multiple)", [
        (aqua, NormalStrategy()),
        (heal, DefensiveStrategy()),
        (trans, AggressiveStrategy()),
    ])


if __name__ == "__main__":
    main()