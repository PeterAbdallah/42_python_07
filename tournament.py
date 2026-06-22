#!/usr/bin/env python3

from ex0.creature import Creature
from ex0.factories import CreatureFactory, FlameFactory, AquaFactory
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategies import (NormalStrategy,
                            AggressiveStrategy,
                            DefensiveStrategy)
from ex2.strategy import BattleStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    # Create fighters using factory
    fighters: list[tuple[Creature, BattleStrategy]] = []
    for fact, strat in opponents:
        creature = fact.create_base()
        fighters.append((creature, strat))

    # Loop through fighters and battle
    for i in range(len(fighters)):
        for j in range(i+1, len(fighters)):
            creature1, strategy1 = fighters[i]
            creature2, strategy2 = fighters[j]

            # Display
            print("\n* Battle *")
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")

            # Validate first creature
            if not strategy1.is_valid(creature1):
                raise Exception(f"Invalid creature '{creature1.name}' \
for this {strategy1.type}")

            # Validate second creature
            if not strategy2.is_valid(creature2):
                raise Exception(f"Invalid creature '{creature2.name}' \
for this {strategy2.type}")

            # Act (action)
            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")


def tournament() -> None:
    # Create factories
    flamefact = FlameFactory()
    healfact = HealingCreatureFactory()
    aquafact = AquaFactory()
    transfact = TransformCreatureFactory()

    # Create strategies
    normal_strat = NormalStrategy()
    aggressive_strat = AggressiveStrategy()
    def_strat = DefensiveStrategy()

    # Create Opponents
    opponents0 = [(flamefact, normal_strat),
                  (healfact, def_strat)]
    opponents1 = [(flamefact, aggressive_strat),
                  (healfact, def_strat)]
    opponents2 = [(aquafact, normal_strat),
                  (healfact, def_strat),
                  (transfact, aggressive_strat)]

    # TOURNAMENT 0
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")
    try:
        battle(opponents0)
    except Exception as e:
        print(f"Battle error, aborting tournament: {e}")

    # TOURNAMENT 1
    print("\nTournament 1 (error)")
    print("[ (Flameling+Agressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")
    try:
        battle(opponents1)
    except Exception as e:
        print(f"Battle error, aborting tournament: {e}")

    # TOURNAMENT 2
    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    print("3 opponents involved")
    try:
        battle(opponents2)
    except Exception as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    tournament()
