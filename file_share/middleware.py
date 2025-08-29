from django.shortcuts import redirect
from django.urls import reverse

class LoginAPIMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Se for GET para /api/login/, redireciona para a página de login
        if request.method == 'GET' and request.path == '/api/login/':
            return redirect(reverse('login-page'))
        
        response = self.get_response(request)
        return response