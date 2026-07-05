import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    scores = []
    for score in sys.argv[1:]:
        try:
            scores.append(int(score))
        except ValueError:
            print(f"Invalid parameter: '{score}'")

    if not scores:
        print("No scores provided. " +
              f"Usage: python3 {sys.argv[0]} <score1> <score2> ..")
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
    print()


if __name__ == "__main__":
    main()
