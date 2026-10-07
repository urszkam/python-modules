import sys
from typing import IO


def read_file(
    executable_name: str,
    files_list: list[str]
) -> None:
    if len(files_list) != 1:
        print(f"Usage: {executable_name} <file>")
        return

    file_name: str = files_list[0]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")

    try:
        fd: IO[str] = open(file_name, "r", encoding="utf-8")
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
        return

    try:
        print("---\n")
        print(fd.read())
        print("\n---")
    except (OSError, UnicodeDecodeError) as e:
        print(f"Error reading file '{file_name}': {e}")
        return
    finally:
        fd.close()
        print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    read_file(sys.argv[0], sys.argv[1:])
