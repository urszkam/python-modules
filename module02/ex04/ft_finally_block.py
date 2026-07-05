class GardenError(Exception):
    def __init__(self, msg: str = "Unknown garden error"):
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Unknown plant error"):
        super().__init__(msg)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else
        raise PlantError()


def test_watering_system() -> None:
    print("Opening Watering System")
    try:
        for plant in args:
    except:

    finally:
        print("Closing watering system")


def main():


if __name__ == "__main__"
    main()