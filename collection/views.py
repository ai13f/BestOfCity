from django.shortcuts import render
from collection.models import Profile

def index(request):
    profiles = Profile.objects.all()
    
    return render(request, 'index.html', {
        'profiles' : profiles,
    })

def profile_detail(request, slug):
	profile = Profile.objects.get(slug=slug)

	return render(request, 'profiles/profile_detail.html', {
		'profile' : profile,
	})