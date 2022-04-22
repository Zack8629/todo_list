from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['username', 'email', 'task_text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['task_text'].widget.attrs.update({'class': 'form-control',
                                                      'style': 'height: 40px'})
