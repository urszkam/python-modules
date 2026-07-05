def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            int('a')
        case 1:
            2 / 0
        case 2:
            open("/non/existent/file", "r")
        case 3:
            "add" + 3


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    cases = (0, 1, 2, 3, 4)

    for case in cases:
        print(f"Testing operation {case}...")
        try:
            garden_operations(case)
        except (
            ValueError, ZeroDivisionError, FileNotFoundError, TypeError
        ) as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        else:
            print("Operation completed successfully")

    print("\nAll error types tested successfully!")


test_error_types()
