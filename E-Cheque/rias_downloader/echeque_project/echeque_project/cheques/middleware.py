from django.shortcuts import redirect
from django.urls import reverse

class RedirectToHomePageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/':
            return redirect(reverse('home'))  # Assuming 'home' is the name of your home URL
        return self.get_response(request)