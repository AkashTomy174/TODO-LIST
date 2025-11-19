from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .forms import ContactForm
from .models import contactMessage
from .forms import RegistrationForm, LoginForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
context = {
    'name': 'akash',
    'age': 21
}


def home(request):
    return render(request, 'home.html',context)

def form_view(request):
    success = False
    saved_message = None
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact_message = form.save()
            print(f"Saved message: {contact_message}")
            success = True
            saved_message = contact_message
            form = ContactForm()  # Reset form after successful submission
    else:
        form = ContactForm()
    return render(request, 'form.html', {'form': form, 'success': success, 'saved_message': saved_message})

def messages_view(request):
    messages = contactMessage.objects.all().order_by('-submitted_at')
    return render(request, 'messages.html', {'messages': messages})

def edit_message(request, id):
    message = get_object_or_404(contactMessage, id=id)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=message)
        if form.is_valid():
            form.save()
            return redirect('messages')
    else:
        form = ContactForm(instance=message)
    return render(request, 'edit_message.html', {'form': form, 'message': message})

def delete_message(request, id):
    message = get_object_or_404(contactMessage, id=id)
    if request.method == 'POST':
        message.delete()
        return redirect('messages')
    return render(request, 'delete_message.html', {'message': message})


def register(request):
    """Custom registration without using Django's UserCreationForm.

    Creates a new `User` after validating the form, sets the password
    using `set_password`, logs the user in, and redirects to `home`.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data.get('email', '')
            password = form.cleaned_data['password1']
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def custom_login(request):
    """Custom login view that does not rely on Django's built-in LoginView.

    Verifies credentials manually and logs the user in on success.
    """
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = None
            if user and check_password(password, user.password):
                login(request, user)
                next_url = request.POST.get('next') or 'home'
                return redirect(next_url)
            else:
                error = 'Invalid username or password'
                # Clear password field when rendering the form again to avoid
                # accidentally showing a value or relying on browser autofill.
                form = LoginForm(initial={'username': username})
    else:
        form = LoginForm()
        # If redirected here after logout, show no error and an informational flag
        if request.GET.get('logged_out'):
            logged_out = True
        else:
            logged_out = False
    return render(request, 'registration/login.html', {'form': form, 'error': error, 'logged_out': logged_out})


def custom_logout(request):
    # Log out the user and redirect to the login page with a flag
    # so the login page can render a fresh (empty) form and show a message.
    logout(request)
    login_url = reverse('login')
    return redirect(f"{login_url}?logged_out=1")

