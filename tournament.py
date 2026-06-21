#!/usr/bin/env python3

from 
from ex0.factories import CreatureFactory, FlameFactory, AquaFactory
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategies import (NormalStrategy,
                            AggressiveStrateg,
                            DefensiveStrategy,
                            BattleStrategy)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]):
    pass


def tournament() -> None:
    flamefact = FlameFactory()
    healfact = HealingCreatureFactory()
    flameli = flamefact.create_base()
    sprout = healfact.create_base()

    # TOURNAMENT 0
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")
    print("\n* Battle *")
    print(flameli.describe())
    print("vs.")
    print(sprout.describe())
    print("now fight!")
    print(flameli.attack())
    print(sprout.attack())
    print(sprout.heal("itself"))

    # TOURNAMENT 1
    print("Tournament 1 (error)")
    print("[ (Flameling+Agressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")
    print("\n* Battle *")
    print(flameli.describe())
    print("vs.")
    print(sprout.describe())
    print("now fight!")
    print(flameli.attack())
    print(sprout.attack())
    print(sprout.heal("itself"))



if __name__ == "__main__":
    tournament()
