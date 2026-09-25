import sys


def main(args: list[str]) -> None:
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")

    if len(args) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args) - 1}")

        idx = 1
        for arg in args[1:]:
            print(f"Argument {idx}: {arg}")
            idx += 1

    print(f"Total arguments: {len(args)}\n")


if __name__ == "__main__":
    main(sys.argv)
