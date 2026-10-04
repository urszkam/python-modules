import random as r
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = [
        "alice", "bob", "charlie", "dylan", "emma", "steven",
        "gregory", "john", "kevin", "liam"
    ]
    actions = [
        "sleep", "eat", "run", "move", "climb", "swim", "dance",
        "grab", "release", "use"
    ]

    while True:
        yield r.choice(players), r.choice(actions)


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while events:
        rand_idx = r.randint(0, len(events) - 1)
        event = events[rand_idx]
        del events[rand_idx]
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    gen = gen_event()
    for i in range(1000):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")

    events = [next(gen) for _ in range(10)]
    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
