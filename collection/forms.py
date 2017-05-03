from django.forms import ModelForm
from collection.models import Profile, Restaurant


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ('name', 'description', 'state')


class RestaurantForm(ModelForm):

    class Meta:
        model = Restaurant
        fields = ('name', 'description', 'category')
