from django.shortcuts import render
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
}


def dish(request, dish):
    template_name = 'calculator/index.html'
    recipe = {}
    context = {'recipe': recipe}

    dish_content = DATA.get(dish)
    if dish_content is None:
        return render(request, template_name, context)

    amount = int(request.GET.get('servings', '1'))

    for key, value in dish_content.items():
        recipe[key] = value * amount

    return render(request, template_name, context)

