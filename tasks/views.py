from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import SuccessURLAllowedHostsMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView, UpdateView

from tasks.forms import TaskCreateForm, TaskUpdateForm
from tasks.models import Task
from .sorting import sorting_tasks


class ContextDataMixin:
    page_title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


class TasksListView(ContextDataMixin, ListView):
    paginate_by = 3
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'
    page_title = 'Все статьи'

    def get_ordering(self):
        get_params = self.request.GET
        if get_params:
            return sorting_tasks(**get_params)
        super(TasksListView, self).get_ordering()


class TaskCreateView(ContextDataMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'tasks_create_form.html'
    page_title = 'Создание задачи'
    success_message = 'Задача успешна создана!'

    def get_success_url(self):
        return reverse_lazy('tasks:index')

    def form_valid(self, form, *args, **kwargs):
        form.save()
        return super(TaskCreateView, self).form_valid(form)


class LoginView(SuccessURLAllowedHostsMixin, FormView):
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'registration/login.html'


class TaskUpdateView(ContextDataMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'tasks_update_form.html'
    page_title = 'Редактирование задачи'
    success_message = 'Задача успешно изменена'

    def get_success_url(self):
        return reverse_lazy('tasks:index')

    def form_valid(self, form, *args, **kwargs):
        instance = form.save(commit=False)
        self.edit_mark(instance)
        instance.save()
        return super(TaskUpdateView, self).form_valid(form)

    def get_text_before_editing(self):
        return self.get_object().task_text

    def edit_mark(self, instance):
        if self.get_text_before_editing() != instance.task_text:
            instance.is_edited = True

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('tasks:login')
        return super(TaskUpdateView, self).dispatch(request, *args, **kwargs)


class TaskDoneView(ContextDataMixin, SuccessMessageMixin, UpdateView):
    model = Task

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('tasks:login')
        elif request.user.is_authenticated:
            self.mark_as_done()
            return redirect('tasks:index')
        return super(TaskDoneView, self).dispatch(request, *args, **kwargs)

    def mark_as_done(self):
        obj = self.get_object()
        obj.is_done = True
        obj.save()
