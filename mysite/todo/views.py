from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem


def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo/todo.html', {'all_items': all_todo_items})

def addTodo(request):
    new_item = TodoItem(content=request.POST['content'])#create a new todo all_items
    new_item.save()#save
    return HttpResponseRedirect('/todo/')#redirect the browser to '/todo/'

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    # new_item = TodoItem(content=request.POST.get('content'))#create a new todo all_items
    # new_item.save()#save
    return HttpResponseRedirect('/todo/')#redirect the browser to '/todo/'
