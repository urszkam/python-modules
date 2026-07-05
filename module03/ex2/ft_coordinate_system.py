import math


def calc_distance(coords1: tuple[float, float, float],
                  coords2: tuple[float, float, float] = (0, 0, 0)) -> float:
    squared_distance = ((coords1[0] - coords2[0])**2 +
                        (coords1[1] - coords2[1])**2 +
                        (coords1[2] - coords2[2])**2)
    return round(math.sqrt(squared_distance), 4)


def get_player_pos() -> tuple[float, float, float]:
    coords: list[float] = []
    while not coords:
        input_coords = input("Enter new coordinates as " +
                             "floats in format 'x,y,z': ")

        str_coords = input_coords.split(",")
        if len(str_coords) != 3:
            print("Invallid syntax")
            continue
        try:
            for coord in str_coords:
                coords.append(float(coord.strip()))
        except ValueError as e:
            print(f"Error on parameter '{coord.strip()}': {e}")
            coords = []
    return coords[0], coords[1], coords[2]


def main() -> None:
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")

    coords1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {coords1}")
    print(f"It includes: X={coords1[0]}, Y={coords1[1]}, Z={coords1[2]}")
    print(f"Distance to center: {calc_distance(coords1)}")

    print("\nGet a second set of coordinates")

    coords2: tuple[float, float, float] = get_player_pos()
    print("Distance between the 2 sets of coordinates:",
          calc_distance(coords1, coords2))


if __name__ == "__main__":
    main()
