from django import forms

from tasks.models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['username', 'email', 'task_text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['task_text'].widget.attrs.update({'class': 'form-control',
                                                      'style': 'height: 40px'})


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['username', 'email', 'task_text', 'is_done']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['task_text'].widget.attrs.update({'class': 'form-control',
                                                      'style': 'height: 40px'})
        self.fields['is_done'].widget.attrs.update({'class': 'form-check'})
