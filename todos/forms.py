from django.forms import ModelForm, Form, BooleanField

from .models import Todo


class TodoModelForm(ModelForm):
    class Meta:
        model = Todo
        # fields = '__all__'
        exclude = ['creator']

    def save(self, user, commit=True):
        todo = super().save(commit=False)
        todo.creator = user
        todo.save()

        self.save_m2m()

        return todo


class DeleteConfirmForm(Form):
    check = BooleanField(label='確定是否刪除?')
