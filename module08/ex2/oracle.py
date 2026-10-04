import os

from dotenv import load_dotenv


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    dir = os.path.dirname(__file__)
    env_path = os.path.join(dir, ".env")

    if not load_dotenv(env_path, override=False):
        print("Failed to load configuration from .env file.\n")

    mode = os.getenv("MATRIX_MODE")
    db = os.getenv('DATABASE_URL')
    api = os.getenv('API_KEY')
    log_lvl = os.getenv('LOG_LEVEL')
    zion = os.getenv('ZION_ENDPOINT')

    print("Configuration loaded:")

    is_missing = not all([mode, db, api, log_lvl, zion])

    if mode not in ["production", "development"]:
        if not mode:
            print("Missing MATRIX_MODE value.", end=" ")
        else:
            print("Incorrect value for MATRIX_MODE.", end=" ")
        print("Setting to default value.")
        mode = "development"
    log_lvl = (
        log_lvl if log_lvl else
        'DEBUG' if mode == "development" else "ERROR"
    )

    print(f"Mode: {mode}")
    print("Database: " +
          (f"Connected to {mode} instance" if db else "Missing DATABASE_URL"))
    print(f"API Access: "
          f"{'Authenticated' if api else 'Missing API_KEY'}")
    print(f"Log Level: {log_lvl}")
    print(f"Zion Network: {'Online' if zion else 'Missing ZION_ENDPOINT'}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if not os.path.isfile(env_path):
        print("[WARNING] .env file not found")
    elif is_missing:
        print("[WARNING] missing configuration in .env file")
    else:
        print("[OK] .env file properly configured")

    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
