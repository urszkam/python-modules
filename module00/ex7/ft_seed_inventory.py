def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.capitalize()

    match unit:
        case "packets":
            print(f"{seed} seeds: {quantity} {unit} available")
        case "grams":
            print(f"{seed} seeds: {quantity} {unit} total")
        case "area":
            print(f"{seed} seeds: covers {quantity} square meters")
        case _:
            print("Unknown unit type")
