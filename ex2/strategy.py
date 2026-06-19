from abc import ABC, abstractmethod
from ex0.creature import Creature


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    # TODO is creature suitable for strategy?
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass
