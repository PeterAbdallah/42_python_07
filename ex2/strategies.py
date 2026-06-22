from typing import Any
from ex0.creature import Creature
from ex1.capabilities import TransformCapability, HealCapability
from ex2.strategy import BattleStrategy


# Simple for all creature that will use attack()
class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        self.type = "Normal Strategy"

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Any) -> None:
        print(creature.attack())


# For creatures with transform capabilities
class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        self.type = "Aggressive Strategy"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise Exception(f"Invalid creature '{creature.name}' \
for this {self.type}")

        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


# For creatures with healing capabilities
class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        self.type = "Defensive Strategy"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, HealCapability):
            raise Exception(f"Invalid creature '{creature.name}' \
for this {self.type}")

        print(creature.attack())
        print(creature.heal("itself"))
