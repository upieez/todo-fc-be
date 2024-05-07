import json
from django.db.models import Max
from django.http import HttpResponse, JsonResponse

# Create your views here.
from .models import Todo

def index(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        filter = request.GET.get('filter')
        if filter == 'active':
            todos = Todo.objects.filter(completed=False)
        elif filter == 'completed':
            todos = Todo.objects.filter(completed=True)
        json_data = json.dumps(list(todos.order_by('order').values()))
        return JsonResponse({'data': json_data})
    elif request.method == 'POST':
        # Get the current maximum order
        max_order = Todo.objects.all().aggregate(Max('order'))['order__max']
        if max_order is None:
            max_order = 0
        data = json.loads(request.body)
        text = data.get('text')
        todo = Todo.objects.create(text=text,order=max_order + 1)
        todo.save()
        return JsonResponse({'data': "todo created"}) 

def update(request, id):
    if request.method == 'PATCH':
        todo = Todo.objects.get(id=id)
        todo.completed = not todo.completed
        todo.save()
        return HttpResponse(f"You're updating todo {id}")
    if request.method == 'DELETE':
        todo = Todo.objects.get(id=id)
        todo.delete()
        return HttpResponse(f"You're deleting todo {id}")

def reorder(request, id):
    return HttpResponse(f"You're reordering todo {id}")


def del_completed(request):
    if request.method == 'DELETE':
        completed_todo = Todo.objects.filter(completed=True)
        completed_todo.delete()
        
    return HttpResponse(f"You're deleting all completed")
