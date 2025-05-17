from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LostItem
from .forms import LostItemForm, RegisterForm

def home(request):
    category = request.GET.get('category', '')
    if category:
        items = LostItem.objects.filter(category=category)
    else:
        items = LostItem.objects.all()
    return render(request, 'home.html', {'items': items, 'category': category})

def lost_items(request):
    items = LostItem.objects.filter(category='lost')
    return render(request, 'lost.html', {'items': items})

def found_items(request):
    items = LostItem.objects.filter(category='found')
    return render(request, 'found.html', {'items': items})

def item_detail(request, pk):
    item = LostItem.objects.get(id=pk)
    return render(request, 'item_detail.html', {'item': item})

@login_required
def create_item(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.posted_by = request.user
            item.save()
            return redirect('home')
    else:
        form = LostItemForm()
    return render(request, 'item_form.html', {'form': form})

@login_required
def user_posts(request):
    items = LostItem.objects.filter(posted_by=request.user)
    return render(request, 'user_posts.html', {'items': items})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Contact Form Submission: Name={name}, Email={email}, Message={message}")
        return render(request, 'contact.html', {'message_sent': True})
    return render(request, 'contact.html')