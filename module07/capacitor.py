from ex1 import HealingCreatureFactory, TransformCreatureFactory


if __name__ == "__main__":
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    print("Testing Creature with healing capability")
    basic_h = healing_factory.create_base()
    evolved_h = healing_factory.create_evolved()

    print(" base:")
    print(basic_h.describe())
    print(basic_h.attack())
    print(basic_h.heal())

    print(" evolved:")
    print(evolved_h.describe())
    print(evolved_h.attack())
    print(evolved_h.heal())

    print("\nTesting Creature with transform capability")
    basic_t = transform_factory.create_base()
    evolved_t = transform_factory.create_evolved()

    print(" base:")
    print(basic_t.describe())
    print(basic_t.attack())
    print(basic_t.transform())
    print(basic_t.attack())
    print(basic_t.revert())

    print(" evolved:")
    print(evolved_t.describe())
    print(evolved_t.attack())
    print(evolved_t.transform())
    print(evolved_t.attack())
    print(evolved_t.revert())
