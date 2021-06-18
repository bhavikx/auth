from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm
from django import forms


from .models import User, Profile

class NewUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(save):
        user = super().save(commit=False)
        user.is_user1 = True
        user.save()
        Profile.objects.create(user=user)
        return user

class ChangeProfile(ModelForm):
    class Meta:
        model = Profile
        fields = ["name"]