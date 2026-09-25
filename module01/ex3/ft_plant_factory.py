class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def __str__(self) -> str:
        name = self._name.capitalize()
        return f"{name}: {self._height}cm, {self._age} days old"

    def get_height(self) -> float:
        return self._height

    def grow(self) -> None:
        growth = self._height * (0.01 if self._height > 50 else 0.03)
        self._height = round(self._height + growth, 1)

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(self)


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25.2, 30),
        Plant("Sunflower", 80.0, 45),
        Plant("Cactus", 15.5, 120),
        Plant("Fern", 19.5, 70),
        Plant("Oak", 320.0, 790)
    ]
    for plant in plants:
        print("Created: ", end="")
        plant.show()
