from django.shortcuts import render, redirect
from .models import Recipe

# Create your views here.
def home(request):
    recipe_objs = Recipe.objects.all()
    data = {'recipes':recipe_objs}
    return render(request, 'home.html', context=data)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        process = request.POST.get('process')
        picture = request.FILES.get('picture')
        Recipe.objects.create(name=name,category=category,description=description,ingredients=ingredients,process=process,picture=picture)
        return redirect('home')
    return render(request, 'create.html')