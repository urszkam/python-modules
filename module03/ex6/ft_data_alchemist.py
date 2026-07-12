import random as r


def print_scores() -> None:
    print("=== Game Data Alchemist ===\n")

    players = ["Alice", "bob", "Charlie", "dylan", "Emma",
               "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {players}")

    all_capitalized: list[str] = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capitalized}")

    only_capitalized: list[str] = [
        name for name in players if name == name.capitalize()
    ]
    print(f"New list of capitalized names only: {only_capitalized}\n")

    scores: dict[str, int] = {
        name: r.randint(1, 999) for name in all_capitalized
    }
    print(f"Score dict: {scores}")

    avg = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {avg}")

    high_scores: dict[str, int] = {
        k: scores[k] for k in scores if scores[k] > avg
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    print_scores()
