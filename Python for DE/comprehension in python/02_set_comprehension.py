"""Set comprehensions: build collections of unique values."""


def unique_tea_names(menu: list[str]) -> set[str]:
    """Return unique tea names from a menu."""
    return {tea for tea in menu}


def recipe_spices(recipes: dict[str, list[str]]) -> set[str]:
    """Flatten recipe ingredients into one set of unique spices."""
    return {spice for ingredients in recipes.values() for spice in ingredients}


if __name__ == "__main__":
    recipes = {
        "masala chai": ["ginger", "cardamom", "clove"],
        "elaichi chai": ["cardamom", "milk"],
        "spicy chai": ["ginger", "clove"],
    }
    print("Unique spices:", recipe_spices(recipes))
