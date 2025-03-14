import requests

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from task_manager.models import Task
from task_manager.forms import TaskForm


# view basadas en clases
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        completed_filter = self.request.GET.get('completed')
        if completed_filter:
            return Task.objects.filter(
                completed=(completed_filter.lower() == 'true')
            )
        return Task.objects.all()


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()
        weather_data = None
        if task.city:
            weather_data = fetch_weather(task.city)
        context['weather'] = weather_data
        return context


# View basadas en funciones
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_manager_api:task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create.html', {'form': form})


def mark_task_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.save()
    return redirect('task_manager_api:task_detail', pk=pk)


def fetch_weather(city):
    API_KEY = "6c21465e8c4defcc93e3f6d82761e6ad"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return {
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description']
            }
    except requests.exceptions.RequestException:
        return None
    return None
