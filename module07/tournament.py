from ex0 import AquaFactory, FlameFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
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
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    print("Tournament 0 (basic)")
    battle([
        (flame_factory, normal_strategy),
        (healing_factory, defensive_strategy),
    ])

    print("\nTournament 1 (error)")
    battle([
        (flame_factory, aggressive_strategy),
        (healing_factory, defensive_strategy),
    ])

    print("\nTournament 2 (multiple)")
    battle([
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transform_factory, aggressive_strategy)
    ])
