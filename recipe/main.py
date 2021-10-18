from recipe import Recipe


# replace redundant code with a creational method
def create_recipe(name, chocolate=0, coffee=0, milk=0, sugar=0, price=0.0):
    recipe = Recipe(name)
    recipe.chocolate = chocolate
    recipe.coffee = coffee
    recipe.milk = milk
    recipe.sugar = sugar
    recipe.price = price
    print(recipe)
    return recipe  # Just avoid warning


if __name__ == '__main__':
    recipe1 = Recipe("Coffee with sugar")
    recipe1.coffee = 4
    recipe1.sugar = 2
    recipe1.milk = 0
    recipe1.price = 30.0
    print(recipe1)

    recipe2 = create_recipe("Latte", 0, 2, 1, 2, 40.0)

    recipe3 = create_recipe("Hot Chocolate", 3, 0, 4, 2, 30.0)
