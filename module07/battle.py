from ex0 import AquaFactory, FlameFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    basic = factory.create_base()
    evolved = factory.create_evolved()

    print(basic.describe())
    print(basic.attack())
    print(evolved.describe())
    print(evolved.attack())
    print()


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    base1 = factory1.create_base()
    base2 = factory2.create_base()

    print(base1.describe())
    print(" vs.")
    print(base2.describe())
    print(" fight!")
    print(base1.attack())
    print(base2.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    test_factory(flame_factory)
    test_factory(aqua_factory)
    battle(flame_factory, aqua_factory)
