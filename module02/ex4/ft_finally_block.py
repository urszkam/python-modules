class GardenError(Exception):
    def __init__(self, msg: str = "Unknown garden error") -> None:
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Unknown plant error") -> None:
        super().__init__(msg)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(
    plants: tuple[str, ...] = ("Tomato", "Lettuce", "Carrots")
) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===")

    print("\nTesting valid plants...")
    test_watering_system()

    print("\nTesting invalid plants...")
    test_watering_system(("Tomato", "lettuce", "Carrots"))

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
