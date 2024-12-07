def read_cook_book(filename):
    cook_book = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            ingredients_list = []
            for ingredient in file:
                ingredient = ingredient.strip()
                if not ingredient:
                    break
                ingredient_name, quantity, measure = map(str.strip, ingredient.split('|'))
                ingredients_list.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[dish_name] = ingredients_list
    return cook_book

filename = 'recipes.txt'  # Укажите здесь путь к вашему файлу
cook_book = read_cook_book(filename)
print(cook_book)