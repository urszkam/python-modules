def ft_harvest_total() -> None:
    day = 1
    total = 0

    while day <= 3:
        total += int(input(f"Day {day} harvest: "))
        day += 1

    print(f"Total harvest: {total}")
