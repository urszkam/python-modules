from abc import ABC, abstractmethod

from ex0.creature import Creature
from ex1.transform import TransformCapability
from ex1.healing import HealCapability
from .exception import InvalidStrategyException


class BattleStrategy(ABC):
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name.capitalize()

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("normal")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if (not isinstance(creature, Creature)):
            raise InvalidStrategyException(creature.name, self._name)
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("aggressive")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if (not isinstance(creature, TransformCapability)):
            raise InvalidStrategyException(creature.name, self._name)
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("defensive")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if (not isinstance(creature, HealCapability)):
            raise InvalidStrategyException(creature.name, self._name)
        print(creature.attack())
        print(creature.heal())
