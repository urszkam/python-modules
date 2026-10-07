from alchemy import grimoire


if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print("Testing record light spell: ", end="")
    ingrs = "Earth, wind and fire"
    print(f"{grimoire.light_spell_record('Fantasy', ingrs)}")
