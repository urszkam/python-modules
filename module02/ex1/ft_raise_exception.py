def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)

    max, min = 40, 0
    if min <= temp <= max:
        return temp
    raise ValueError(
        f"{temp}°C is too {'hot' if temp > max else 'cold'} for plants " +
        f"({f'max {max}' if temp > max else f'min {min}' }°C)")


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")
    cases = ("25", "abc", "100", "-50")

    for case in cases:
        print(f"Input data is '{case}'")
        try:
            temp = input_temperature(case)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
