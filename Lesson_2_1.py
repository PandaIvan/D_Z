recipes = """
Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г

Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт
"""
with open('recipes.txt', 'w') as file:
  file.write(recipes.strip())

with open('recipes.txt', 'r') as file:
  for line in file:
    print(line.strip())


cook_book1 = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }

with open('cook_book.txt', 'w', encoding='utf-8') as file:
  for dish, ingredients in cook_book1.items():
    file.write(f'{dish}\n')
    file.write(f'{len(ingredients)}\n')

    for ingredient in ingredients:
      file.write(f"{ingredient['ingredient_name']} | {ingredient['quantity']} | {ingredient['measure']}\n")


print("'cook_book.txt' успех")


def load_cook(filename):
  cook_book = {}
  with open(filename, 'r', encoding='utf-8') as file:
    while True:
      dish_name = file.readline().strip()
      if not dish_name:
        break

      ingredient_count = int(file.readline().strip())
      ingredients = []
      for _ in range(ingredient_count):
        ingredient_line = file.readline().strip()
        ingredient_name, quantity_str, measure = ingredient_line.split(' | ')
        quantity = int(quantity_str)
        ingredients.append({
          'ingredient_name': ingredient_name,
          'quantity': quantity,
          'measure': measure
        })
      cook_book[dish_name] = ingredients

  return cook_book

def by_dishes(dishes, person_count, cook_book):
  shop_list = {}
  for dish in dishes:
    if dish in cook_book:
      for ingredient in cook_book[dish]:
        ingredient_name = ingredient['ingredient_name']
        quantity = ingredient['quantity'] * person_count
        measure = ingredient['measure']

        if ingredient_name in shop_list:
          shop_list[ingredient_name]['quantity'] += quantity
        else:
          shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
  return shop_list



cook_book = load_cook('cook_book.txt')

result = by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)

for ingredient, details in result.items():
    print(f"{ingredient}: {details['quantity']} {details['measure']}")


import os


def count_lines_and_write(directory, output_file):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_name in files:
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'r', encoding='utf-8') as in_file:
                lines = in_file.readlines()
                num_lines = len(lines)

            out_file.write(f'{file_name}\n{num_lines}\n')

            for line_number, _ in enumerate(lines, start=1):
                out_file.write(f'Строка номер {line_number} файла {file_name}\n')


directory = r'C:\Users\Oxoth\OneDrive\Рабочий стол\Dz\Dz_2'
output_file = r'C:\Users\Oxoth\OneDrive\Рабочий стол\Dz\output.txt'
count_lines_and_write(directory, output_file)



