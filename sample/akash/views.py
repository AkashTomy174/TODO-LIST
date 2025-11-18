from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from .models import contactMessage

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

