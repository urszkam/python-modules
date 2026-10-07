from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = light_spell_allowed_ingredients()
    result = "INVALID"

    for allowed in allowed_ingredients:
        if allowed.lower() in ingredients.lower():
            result = "VALID"
            break

    return f"{ingredients} - {result}"
