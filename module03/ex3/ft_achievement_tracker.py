import random as r


def gen_player_achievements(all_achievements: list[str]) -> set[str]:
    achievements_number = r.randint(1, len(all_achievements))
    chosen_achievements = r.sample(all_achievements, achievements_number)

    return set(chosen_achievements)


def main() -> None:
    all_achievements = [
        "First Spell", "Magic Book", "Hidden Rune", "Fire Trial", "Ice Cave",
        "Storm Call", "Moon Charm", "Star Dust", "Potion Time",
        "Flying Broom", "Magic Mirror", "Lost Wand", "Crystal Cave",
        "Dragon Egg", "Magic Tower", "Broken Spell"
    ]

    print("=== Achievement Tracker System ===\n")
    alice: set[str] = gen_player_achievements(all_achievements)
    bob: set[str] = gen_player_achievements(all_achievements)
    sarah: set[str] = gen_player_achievements(all_achievements)
    sam: set[str] = gen_player_achievements(all_achievements)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Sarah: {sarah}")
    print(f"Player Sam: {sam}")

    distinct_achievements: set[str] = alice | bob | sarah | sam
    print(f"\nAll distinct achievements: {distinct_achievements}")

    common_achievements: set[str] = alice & bob & sarah & sam
    print(f"\nCommon achievements: {common_achievements}\n")

    print(f"Only Alice has: {alice - (bob | sarah | sam)}")
    print(f"Only Bob has: {bob - (alice | sarah | sam)}")
    print(f"Only Sarah has: {sarah - (alice | bob | sam)}")
    print(f"Only Sam has: {sam - (alice | bob | sarah)}")
    print()

    print(f"Alice is missing: {set(all_achievements) - alice}")
    print(f"Bob is missing: {set(all_achievements) - bob}")
    print(f"Sarah is missing: {set(all_achievements) - sarah}")
    print(f"Sam is missing: {set(all_achievements) - sam}")


if __name__ == "__main__":
    main()
