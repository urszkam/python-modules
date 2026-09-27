from abc import ABC, abstractmethod

from ex0.creature import Creature
from ex0.creature_factory import CreatureFactory


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass


class Sprouting(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Sprouting", "Grass")
        HealCapability.__init__(self)

    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self._name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")
        HealCapability.__init__(self)

    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self._name} heals itself and others for a large amount"


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sprouting:
        return Sprouting()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()
