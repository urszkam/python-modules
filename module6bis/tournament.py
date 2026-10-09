from ex3 import FlameFactory, CreatureFactory, TransformCreatureFactory
from ex4 import (
    NormalStrategy,
    AggressiveStrategy,
    BattleStrategy,
    InvalidStrategyException
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")

    num_opponents = len(opponents)
    print(f"{num_opponents} opponents involved")

    try:
        for opp1_idx in range(num_opponents):
            for opp2_idx in range(opp1_idx + 1, num_opponents):
                factory1, strategy1 = opponents[opp1_idx]
                factory2, strategy2 = opponents[opp2_idx]

                creature1 = factory1.create_base()
                creature2 = factory2.create_base()

                print("\n* Battle *")
                print(creature1.describe())
                print(" vs.")
                print(creature2.describe())
                print(" now fight!")

                strategy1.act(creature1)
                strategy2.act(creature2)

    except InvalidStrategyException as e:
        print(e)


if __name__ == "__main__":
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()

    print("Tournament 0 (basic)")
    battle([
        (flame_factory, normal_strategy),
        (transform_factory, aggressive_strategy),
    ])

    print("\nTournament 1 (error)")
    battle([
        (transform_factory, aggressive_strategy),
        (flame_factory, aggressive_strategy),
    ])

    print("\nTournament 2 (multiple)")
    battle([
        (flame_factory, normal_strategy),
        (transform_factory, aggressive_strategy),
        (transform_factory, aggressive_strategy)
    ])
