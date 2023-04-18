from django.http import HttpResponse
from django.shortcuts import render

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

def recipe_view(request, recipe_name):
    if recipe_name not in DATA:
        return HttpResponse('Введена некорректная страница! Введите в строке браузера название блюда и количество порций в формате: .../buter/?portion=1')
    recipe = DATA[recipe_name].copy()


    try:
        portion = int(request.GET.get('portion', 0))
    except ValueError:
        portion = 0
        # return HttpResponse('введено неверное количество, введите число!')

    for ing in recipe:
        recipe[ing] *= portion

    context = {
                    'recipe': recipe,
                    'message': 'Введите корректно количество порций в строке в формате: (.../buter/?portion=1) ',
                    'porcia': portion,
                    'meal': recipe_name
              }

    return render(request, 'index.html', context)

def main_page(request):
    return HttpResponse('Введите в строке браузера название блюда и количество порций в формате: .../buter/?portion=1')