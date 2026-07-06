def secure_archive(
    file_name: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    if action == "read":
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                content = f.read()
        except OSError as e:
            return False, f"[Errno {e.errno}] {e.strerror}: '{e.filename}'"
        else:
            return True, content

    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(content)
    except OSError as e:
        return False, f"[Errno {e.errno}] {e.strerror}: '{e.filename}'"
    else:
        return True, "Content successfully written to file"


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("priv.txt"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(success_tuple := secure_archive("file.txt"))

    print("\nUsing 'secure_archive' to write previous content to a new file")
    print(secure_archive("file2.txt", "write", success_tuple[1]))

    print("\nUsing 'secure_archive' to write previous content " +
          "to an inaccessible file")
    print(secure_archive("priv.txt", "write", success_tuple[1]))
