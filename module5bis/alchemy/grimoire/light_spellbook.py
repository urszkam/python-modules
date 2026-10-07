def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients

    val_result = validate_ingredients(ingredients)
    status = "recorded" if val_result.endswith(" - VALID") else "rejected"

    return f"Spell {status}: {spell_name.capitalize()} ({val_result})"
