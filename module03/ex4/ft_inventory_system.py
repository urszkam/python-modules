import sys


def populate_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for arg in args:
        try:
            key, value = arg.split(":")
            key, value = key.strip(), value.strip()
            if not key:
                raise ValueError()
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
            continue

        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue

        try:
            inventory[key] = int(value)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")

    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inv: dict[str, int] = populate_inventory(sys.argv[1:])
    print(f"Got inventory: {inv}")
    print(f"Item list: {list(inv.keys())}")

    total: int = sum(inv.values())
    print(f"Total quantity of the {len(inv)} items: {total}")

    if inv:
        most: str = list(inv.keys())[0]
        least: str = list(inv.keys())[0]
        for key in inv:
            percentage: float = 0.0 if not total else inv[key] / total * 100
            print(f"Item {key} represents {round(percentage, 1)}%")
            if inv[key] > inv[most]:
                most = key
            if inv[key] < inv[least]:
                least = key

        print(f"Item most abundant: {most} with quantity {inv[most]}")
        print(f"Item least abundant: {least} with quantity {inv[least]}")

    inv["magic_item"] = 1
    print(f"Updated inventory: {inv}")
