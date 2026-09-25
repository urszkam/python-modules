class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def increment_grow_calls(self) -> None:
            self._grow_calls += 1

        def increment_age_calls(self) -> None:
            self._age_calls += 1

        def increment_show_calls(self) -> None:
            self._show_calls += 1

        def show(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )

    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)
        self._stats = self.Stats()

    def __str__(self) -> str:
        name = self._name.capitalize()
        return f"{name}: {self._height}cm, {self._age} days old"

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height < 0:
            print(
                f"{self._name.capitalize()}: Error, height can't be negative"
            )
        else:
            self._height = height

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
        else:
            self._age = age

    def grow(self) -> None:
        self._stats.increment_grow_calls()
        growth = self._height * (0.01 if self._height > 50 else 0.03)
        self._height = round(self._height + growth, 2) if growth > 0 else 1

    def age(self) -> None:
        self._stats.increment_age_calls()
        self._age += 1

    def show(self) -> None:
        self._stats.increment_show_calls()
        print(self)

    def show_stats(self) -> None:
        self._stats.show()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous_plant(cls) -> "Plant":
        return cls(name="Unknown plant")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._has_bloom = False

    def get_color(self) -> str:
        return self._color

    def set_color(self, color: str) -> None:
        self._color = color

    def get_has_bloom(self) -> bool:
        return self._has_bloom

    def bloom(self) -> None:
        self._has_bloom = True

    def __str__(self) -> str:
        msg_bloom = "is blooming beautifully!"
        msg_not_bloom = "has not bloomed yet"

        return (
            super().__str__()
            + f"\n Color: {self._color}"
            + f"\n {self._name.capitalize()} "
            + f"{msg_bloom if self._has_bloom else msg_not_bloom}"
        )


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def __str__(self) -> str:
        return super().__str__() + f"\n Seeds: {self._seeds}"


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def __str__(self) -> str:
        return (
            super().__str__()
            + f"\n Harvest Season: {self._harvest_season}"
            + f"\n Nutritional Value: {self._nutritional_value}"
        )

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def increment_shade_calls(self) -> None:
            self._shade_calls += 1

        def show(self) -> None:
            super().show()
            print(f" {self._shade_calls} shade")

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        self._stats: Tree.Stats
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def set_trunk_diameter(self, trunk_diameter: float) -> None:
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self._stats.increment_shade_calls()
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and {self._trunk_diameter}cm wide."
        )

    def __str__(self) -> str:
        return (
            super().__str__()
            + f"\n Trunk Diameter: {self._trunk_diameter}cm"
        )


def display_statistics(plant: Plant) -> None:
    plant.show_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 25, 30, "yellow")
    rose.show()
    display_statistics(rose)
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 320, 790, 25)
    oak.show()
    display_statistics(oak)
    oak.produce_shade()
    display_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show()
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 10, 15, "August")
    tomato.show()
    tomato.grow()
    tomato.age()
    tomato.show()
    display_statistics(tomato)

    print("\n=== Anonymous")
    plant = Plant.create_anonymous_plant()
    plant.show()
    display_statistics(plant)
