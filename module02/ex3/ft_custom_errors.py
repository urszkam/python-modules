class GardenError(Exception):
    def __init__(self, msg: str = "Unknown garden error") -> None:
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Unknown plant error") -> None:
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg: str = "Unknown water error") -> None:
        super().__init__(msg)


def water_plants(is_tank_full: bool) -> None:
    if not is_tank_full:
        raise WaterError("Not enough water in the tank")
    print("Plants watered. Tank is now empty.")


def examine_tomato(is_drought: bool) -> None:
    if is_drought:
        raise PlantError("The tomato plant is wilting!")
    print("The tomato plant is ok.")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting normal operations...")
    try:
        examine_tomato(is_drought=False)
        water_plants(is_tank_full=True)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nTesting PlantError...")
    try:
        examine_tomato(is_drought=True)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print("\nTesting WaterError...")
    try:
        water_plants(is_tank_full=False)
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print("\nTesting GardenError...")
    try:
        water_plants(is_tank_full=False)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        examine_tomato(is_drought=True)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
