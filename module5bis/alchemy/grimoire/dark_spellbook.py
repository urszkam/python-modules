from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    val_result = dark_validate_ingredients(ingredients)
    status = "recorded" if val_result.endswith(" - VALID") else "rejected"

    return f"Spell {status}: {spell_name.capitalize()} ({val_result})"
