from django.db.models import fields
from django.forms import ModelForm
from .models import *

class StaffForm(ModelForm):
    class Meta:
        model=Staff
        fields='__all__'

class ChildrenForm(ModelForm):
    class Meta:
        model=Children
        fields='__all__'

class BlogForm(ModelForm):
    class Meta:
        model=Blog
        fields='__all__'

class GroupForm(ModelForm):
    class Meta:
        model=Group
        fields='__all__'

class MealsForm(ModelForm):
    class Meta:
        model=Meals
        fields='__all__'

class PictureForm(ModelForm):
    class Meta:
        model=Gallery
        fields='__all__'