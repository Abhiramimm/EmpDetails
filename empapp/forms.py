from django import forms

from empapp.models import Category,Employee

class CategoryForm(forms.ModelForm):

    class Meta:

        model=Category

        fields="__all__"

class EmployeeForm(forms.ModelForm):

    class Meta:

        model=Employee

        fields="__all__"
