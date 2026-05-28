from http.client import responses

from .models import Task, Projects, People
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView

from .forms import ProjectForm, RegisterForm

class ProjectsNameView(ListView):
    model = Projects
    template_name = 'projects/project_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Projects.objects.all()


class ProjectDetailView(DetailView):
    model = Projects
    template_name = 'projects/project_list.html'

    def get_queryset(self):
        return Projects.objects.all()


class ProjectCreateView(CreateView):
    model = Projects
    form_class = ProjectForm
    template_name = 'projects/project_form.html'

class ProjectUpdateView(UpdateView):
    model = Projects
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    #place = self.get_object()

class ProjectDeleteView(DeleteView):
    model = Projects
    template_name = 'projects/project_delete.html'

class RegisterView(CreateView):
    form_class = RegisterForm
    template_view = 'reg/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

