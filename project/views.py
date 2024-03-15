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

def edit(request,pk):
    recipe_obj = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        process = request.POST.get('process')
        picture = request.FILES.get('picture')
        recipe_obj.name = name
        recipe_obj.category = category
        recipe_obj.description = description
        recipe_obj.ingredients = ingredients
        recipe_obj.process = process
        recipe_obj.picture = picture
        recipe_obj.save()
        return redirect('home')
    data = {'recipe': recipe_obj}
    return render(request, 'edit.html', context=data)

def delete(request,pk):
    recipe_obj = Recipe.objects.get(id=pk)
    recipe_obj.delete()
    return redirect('home')

def delete_all(request):
    recipe_obj = Recipe.objects.all()
    if request.method == 'POST':
        recipe_obj.delete()
        return redirect('home')
    return render(request, 'delete_all.html')