class Plant:
    def __init__(self, name: str, height: float = 0, age: int = 0) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def __str__(self) -> str:
        name = self._name.capitalize()
        return f"{name}: {self._height}cm, {self._age} days old"

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if (height < 0):
            print(
                f"{self._name.capitalize()}: Error, height can't be negative"
            )
        else:
            self._height = height if height >= 0 else 0

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if (age < 0):
            print(f"{self._name.capitalize()}: Error, age can't be negative")
        else:
            self._age = age if age >= 0 else 0

    def grow(self) -> None:
        growth = self._height * (0.01 if self._height > 50 else 0.03)
        self._height = round(self._height + growth, 2) if growth > 0 else 1

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(self)


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

        return (super().__str__() +
                f"\n Color: {self._color}" +
                f"\n {self._name.capitalize()} " +
                f"{msg_bloom if self._has_bloom else msg_not_bloom}")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def __str__(self) -> str:
        return (super().__str__() +
                f"\n Harvest Season: {self._harvest_season}"
                f"\n Nutritional Value: {self._nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def set_trunk_diameter(self, trunk_diameter: float) -> None:
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of " +
              f"{self._height}cm long and {self._trunk_diameter}cm wide.")

    def __str__(self) -> str:
        return (super().__str__() +
                f"\n Trunk Diameter: {self._trunk_diameter}cm")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 25, 30, "yellow")
    rose.show()
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 320, 790, 25)
    oak.show()
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 10, 15, "August")
    tomato.show()
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
