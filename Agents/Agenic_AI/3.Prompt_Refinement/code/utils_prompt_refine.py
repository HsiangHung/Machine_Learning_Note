import jinja2
from typing import Any

# Define common dietary restrictions
dietary_restrictions = [
    "vegetarian",
    "vegan",
    "gluten-free",
    "dairy-free",
    "nut-free",
    "egg-free",
    "low-sodium",
    "keto",
    "paleo",
    "kosher",
]


def format_prompt(recipe: dict[str, Any], prompt: str) -> str:
    ingredients_str: str = "\n".join(
        ["- " + ingredient for ingredient in recipe["ingredients"]]
    )
    instructions_str: str = "\n".join(
        [
            f"{i + 1}. {instruction}"
            for i, instruction in enumerate(recipe["instructions"])
        ]
    )
    restrictions_str: str = ", ".join(dietary_restrictions)

    return jinja2.Template(prompt).render(
        recipe_name=recipe["name"],
        recipe_ingredients=ingredients_str,
        recipe_instructions=instructions_str,
        dietary_restrictions=restrictions_str,
    )