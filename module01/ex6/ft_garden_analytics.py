class Plant:
    def __init__(self, name: str, height: float, age: int):
        set_name(name)
        set_height(height)
        set_age(age)

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name.capitalize()

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        self._height = heigh if height >= 0 else 0
    
    def get_age(self,) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        self._age = age if age >= 0 else 0

    def __str__(self):
        return f"{self._name}: {self._height}cm, {self._age} days old"

    def show(self) -> None:
        print(f"Created {self}")
    
    def grow(self)

    def age(self)

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return (age > 365)

    def create_anonymous_plant() -> Plant:
        return Plant(name="Unknown plant", height=0, age=0)



class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        set_color(color)
        self._has_bloom = False

    def get_color(self) -> str:
        return self._color

    def set_color(self, color: str) -> None:
        self._color = color

    def get_has_bloom(self) -> bool:
        return self._bloom
    
    def bloom(self):
        self._has_bloom = True

    def __str__(self):
        msg_bloom = "is blooming beautifully!"
        msg_not_bloom = "has not bloomed yet"
        return super().__str__ + 
               f"\n Color: {self._color}" +
               f"\n {self._name} " +
               f"{msg_bloom if self._has_bloom else msg_not_bloom}"


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def __str__(self):
        return super().__str__ + 
               f"\n Harvest Season: {self._harvest_season}"
               f"\n Nutritional Value: {self._nutritional_value}"

class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float):
        super().__init__(name, height, age)
        set_trunk_diameter(trunk_diameter)

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def set_trunk_diameter(self, trunk_diameter: float) -> None
        self._trunk_diameter = trunk_diameter
    
    def produce_shade(self):
        print(f"Tree {self._name} now produces a shade of " +
              f"{self._height}cm long and {self._trunk_diameter}cm wide.")

    def __str__(self):
        return super().__str__ + 
               f"\n Trunk Diameter: {self._trunk_diameter}cm"

if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.is_older_than_year(30)
    Plant.is_older_than_year(400)

    print("\n=== Flower")
    rose = Flower("Rose", 25, 30, "yellow")
    rose.show()
    # rose.show_stats()
    rose.show()
    rose.bloom()
    # rose.show_stats()
    
    print("\n=== Tree")
    oak = Tree("Oak", 320, 790, 25)
    oak.show()
    # oak.show_stats()
    oak.produce_shade()
    # oak.show_stats()

    print("\n=== Seed")


    plant = create_anonymous_plant()
    plant.show()
    # plant.show_stats()