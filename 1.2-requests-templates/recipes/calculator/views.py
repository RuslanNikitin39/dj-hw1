from django.shortcuts import render, reverse
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def dish_view(request, dish):
    servings = request.GET.get('servings', 1)
    context = get_context(dish, int(servings))
    return render(request, 'calculator/index.html', context)


def get_context(dish, servings):
    context = {}
    recipe = DATA.get(dish)
    if recipe == None:
        return context
    context['recipe'] = {}
    compound = {}
    for item in recipe.items():
        compound[item[0]] = item[1] * servings
    context['recipe'] = compound
    return context
