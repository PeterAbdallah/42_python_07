from ex2.strategy import BattleStrategy
from ex0.creature import Creature
from ex1.capabilities import TransformCapability, HealCapability
from typing import Any


# Simple for all creature that will use attack()
class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Any) -> None:
        creature.attack()


# For creatures with transform capabilities
class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise Exception(f"Invalid creature {creature.name} \
for this Defensive startegy")

        creature.transform()
        creature.attack()
        creature.revert()


# For creatures with healing capabilities
class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, HealCapability):
            raise Exception(f"Invalid creature {creature.name} \
for this DefensiveStrategy")

        creature.attack()
        creature.heal("itself")
