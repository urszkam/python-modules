import importlib


def check_dependencies() -> bool:
    print("Checking dependencies:")
    dependencies = {
        'pandas': 'Data manipulation',
        'numpy': 'Numerical computation'
    }
    import_success = True
    for name, description in dependencies.items():
        try:
            module = importlib.import_module(name)
            print(
                f"[OK] {module.__name__} ({module.__version__}) - "
                f"{description} ready"
            )
        except ImportError:
            import_success = False
            print(f"Missing dependency: {name}")
            print("Installation instruction:")
            print("Poetry: poetry -C ex0 install")
            print("Pip: python3 -m pip install -r ex0/requirements.txt")

    return import_success


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    import_success = check_dependencies()

    if import_success:
        print("\nAll reagents present and accounted for.")


if __name__ == "__main__":
    main()
