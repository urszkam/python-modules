import sys


def main(args: list[str]) -> None:
    print("=== Player Score Analytics ===")

    scores = []
    for score in args[1:]:
        try:
            scores.append(int(score))
        except ValueError:
            print(f"Invalid parameter: '{score}'")

    if not scores:
        print("No scores provided. " +
              f"Usage: python3 {args[0]} <score1> <score2> ..")
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
    main(sys.argv)
