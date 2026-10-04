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
        if (age < 0 and self):
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


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Rose", 20, 40)
    print("Plant created: ", end="")
    plant.show()

    plant.set_height(25)
    print(f"Height updated: {plant.get_height()}cm")
    plant.set_age(30)
    print(f"Age updated: {plant.get_age()} days")

    plant.set_height(-25)
    print("Height update rejected")
    plant.set_age(-30)
    print("Age update rejected")

    print("Current state: ", end="")
    plant.show()
