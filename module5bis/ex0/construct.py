import os
import site
import sys


def print_venv_fail() -> None:
    msg = ("\nWARNING: You're in the global environment!\n"
           "The machines can see everything you install.\n\n"
           "To enter the construct, run:\n"
           " python -m venv matrix_env\n"
           " source matrix_env/bin/activate # On Unix\n"
           " matrix_env\\Scripts\\activate # On Windows\n\n"
           "Then run this program again.")
    print(msg)


def print_venv_success() -> None:
    msg = ("\nSUCCESS: You're in an isolated environment!\n"
           "Safe to install packages without affecting\n"
           "the global system.\n")
    print(msg)


def main() -> None:
    python: str = sys.executable
    venv_path: str = sys.prefix if sys.prefix != sys.base_prefix else ''
    venv: str = os.path.basename(venv_path)
    status = "Welcome to the construct" if venv else "You're still plugged in"
    print(f"\nMATRIX STATUS: {status}\n")
    print(
        f"Current Python: {python if python else 'None detected'}"
    )
    print(f"Virtual Environment: {venv if venv else 'None detected'}")

    global_paths = site.getsitepackages([sys.base_prefix])
    print(f"Global package locations: {', '.join(global_paths)}")

    if not venv:
        print_venv_fail()
        return

    print(f"Environment Path: {venv_path}")
    print_venv_success()
    paths = [p for p in site.getsitepackages() if "site-packages" in p]
    print(f"Package installation path:\n {', '.join(paths)}")


if __name__ == "__main__":
    main()
