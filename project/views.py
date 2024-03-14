from django.shortcuts import render
from .models import Recipe

# Create your views here.
def home(request):
    recipe_objs = Recipe.objects.all()
    data = {'recipes':recipe_objs}
    return render(request, 'home.html', context=data)