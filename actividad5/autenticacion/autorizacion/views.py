from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout
from django.shortcuts import redirect


def home(request):
    return render(request, 'home.html')

@user_passes_test(lambda u: u.is_superuser, login_url='home')
def admin_page(request):
    return render(request, 'admin_page.html')

def logout_view(request):
    logout(request)
    return redirect('login')