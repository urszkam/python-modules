from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = dark_spell_allowed_ingredients()
    result = "INVALID"

    for allowed in allowed_ingredients:
        if allowed.lower() in ingredients.lower():
            result = "VALID"
            break

    return f"{ingredients} - {result}"
