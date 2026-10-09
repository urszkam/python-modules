from ex3 import TransformCreatureFactory


if __name__ == "__main__":
    transform_factory = TransformCreatureFactory()

    print("Testing Creature with transform capability")
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
