from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'city']

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < self.cleaned_data.get('created_at').date():
            raise forms.ValidationError("Due date must be in the future.")
        return due_date
