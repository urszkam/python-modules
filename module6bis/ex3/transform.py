from abc import ABC, abstractmethod

from .creature import Creature
from .creature_factory import CreatureFactory


class TransformCapability(ABC):
    def __init__(self) -> None:
        self._transformed = False

    def set_transformed(self, is_transformed: bool) -> None:
        self._transformed = is_transformed

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} performs a boosted strike!"
        return f"{self._name} attacks normally."

    def transform(self) -> str:
        self.set_transformed(True)
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        self.set_transformed(False)
        return f"{self._name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} unleashes a devastating morph strike!"
        return f"{self._name} attacks normally."

    def transform(self) -> str:
        self.set_transformed(True)
        return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.set_transformed(False)
        return f"{self._name} stabilizes its form."


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
