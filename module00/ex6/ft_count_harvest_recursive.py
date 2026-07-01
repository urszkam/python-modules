def _print_days(days: int, curr_day: int = 1) -> None:
    if curr_day > days:
        print("Harvest time!")
        return

    print(f"Day {curr_day}")

    _print_days(days, curr_day + 1)


def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))

    _print_days(days)
