import sys
from typing import IO


def _read_file_content(file: str) -> str:
    try:
        fd: IO[str] = open(file, "r", encoding="utf-8")
    except OSError as e:
        print(f"Error opening file '{file}': {e}")
        raise

    try:
        return fd.read()
    except OSError as e:
        print(f"Error reading file '{file}': {e}")
        raise
    finally:
        fd.close()
        print(f"File '{file}' closed.")


def _print_content(content: str) -> None:
    print("---\n")
    print(content)
    print("\n---")


def _transform_content(content: str) -> str:
    new_content = ""
    for char in content:
        new_content += char if char != "\n" else "#\n"
    if new_content and new_content[-1] != "\n":
        new_content += "#"
    return new_content


def _save_file(content: str, file_name: str) -> None:
    print(f"Saving data to '{file_name}'")

    try:
        fd: IO[str] = open(file_name, "w", encoding="utf-8")
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
        print("Data not saved.")
        return

    try:
        fd.write(content)
    except OSError as e:
        print(f"Error saving data '{file_name}': {e}")
        print("Data not saved.")
    else:
        print(f"Data saved in file '{file_name}'.")
    finally:
        fd.close()


def create_archive(
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
        content: str = _read_file_content(file_name)
    except OSError:
        return

    _print_content(content)

    print("Transform data:")

    transformed_content: str = _transform_content(content)
    _print_content(transformed_content)

    new_file = input("Enter new file name (or empty): ")
    if not new_file:
        print("Not saving data.")
        return

    _save_file(transformed_content, new_file)


if __name__ == "__main__":
    create_archive(sys.argv[0], sys.argv[1:])
