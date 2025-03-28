from django.shortcuts import render


# Create your views here.
def index(request):
    render(request,"myapp/index.html",{})
    from .models import Task
    from django.http import HttpResponse

    def task_list(request):
        tasks = Task.objects.all()
        return render(request, 'todo/task_list.html', {'tasks': tasks})

    def add_task(request):
        if request.method == 'POST':
            title = request.POST.get('title')
            if title:
                Task.objects.create(title=title)
            return redirect('task_list')
        return render(request, 'todo/add_task.html')

    def delete_task(request, task_id):
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('task_list')
