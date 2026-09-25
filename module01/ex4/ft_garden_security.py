class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        set_height(height)
        set_age(age)

    def get_height() -> float:
        return self._height

    def set_height(height: float) -> None:
        self._height = heigh if height >= 0 else 0
    
    def get_age() -> int:
        return self._age

    def set_age(age: int) -> None:
        self._age = age if age >= 0 else 0

    def __str__(self):
        name = self._name.capitalize()
        return f"{name}: {self._height}cm, {self._age} days old"

    def show(self) -> None:
        print(f"Created {self}")
    
    def grow(self)

    def age(self)



if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
        Plant("Fern", 19, 70),
        Plant("Oak", 320, 790)
    ]
    for plant in plants:
        plant.show()
