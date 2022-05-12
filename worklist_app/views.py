from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import List
from .forms import ListForm

# Displays the homepage
def home(request, sorting='date'):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('The item has been added to list successfully!'))
            all_items = List.objects.all().order_by(sorting)
            print (all_items)
            return render(request, 'home.html', {'all_items': all_items})    
    else:
        all_items = List.objects.all().order_by(sorting)
        return render(request, 'home.html', {'all_items': all_items})

# Delete function for task
def delete(request, item_id):
    item = List.objects.get(pk=item_id)
    item.delete()
    messages.success(request, ('The item has been deleted successfully!'))
    return redirect('home')

# Set task selected to pending
def cross_off(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = True
    item.save()
    return redirect('home')

# 
# def uncross(request, item_id):
#     item = List.objects.get(pk=item_id)
#     item.completed = False
#     item.save()
#     return redirect('home')

# Adds new tasks
def add(request):
    if request.method == "POST":
        text = request.POST["item"]
        if text == "":
            messages.error(request, ('You need to write something'))
            return redirect('home') 
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('The Task has been added successfully!'))
        else:
            messages.error(request, ('Please fill in all fields'))
        return redirect('home')   

# Edit tasks
def edit(request, item_id):
    if request.method == "POST":
        item = List.objects.get(pk=item_id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('The item has been edited successfully!'))
            return redirect('home')   
    else:
        item = List.objects.get(pk=item_id)
        return render(request, 'edit.html', {'item': item})

#Sort task list by date
def sort_date(request):
    return home(request, 'date')
#Sort task list by ascending order alphabetically
def sort_ascending(request):
    return home(request, 'item')
#Sort task list by descending order alphabetically
def sort_descending(request):
    return home(request, '-item')
#Sort task list by pending tasks
def sort_pending(request):
    return home(request, '-completed')