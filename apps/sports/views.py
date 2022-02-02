from email import message
from django.shortcuts import redirect, render, reverse

from .models import Users
from .forms import FilterForm, UsersForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        users = UsersForm(request.POST)
        if users.is_valid():
            create = users.save(commit = False)
            create.save()
            return redirect(reverse('sports:index'))
        else:
            return render(request, 'sports/index.html', {'form': users})
    else:
        form = UsersForm()
        return render(request, 'sports/index.html', {'form': form})

def create(request):
    if request.method == 'POST':
        users = UsersForm(request.POST)
        if users.is_valid():
            Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],\
                gender=request.POST['gender'], image=request.POST['image'], sport=request.POST['sport'])
            print('User successfully created')
            messages.success(request, 'User successfully created', extra_tags='create_success')
            return redirect(reverse('sports:index'))
        else: return redirect(reverse('sports:index'))

def search(request):
    if request.method == 'POST':
        users = Users.objects.all()[0:int(request.POST['records'])]
        return render(request, 'sports/users.html', {'users': users})

def find(request):
    if request.method == 'POST':
        filters = FilterForm(request.POST)
        if filters.is_valid():
            return redirect(reverse('sports:find'))
    else:
        filters = FilterForm() 
    return render(request, 'sports/find.html', {'form': filters})

def filter(request):
    if request.method == 'POST':
        users = Users.objects.all()
        if len(request.POST['name']) > 0:
            users = users.filter(first_name__startswith = request.POST['name']) | \
            users.filter(last_name__startswith = request.POST['name'])
        genders = request.POST.getlist('gender')
        if len(genders) > 0: users = users.filter(gender__in = genders)
        sports = request.POST.getlist('sport')
        if len(sports) > 0: users = users.filter(sport__in = sports)
        return render(request, 'sports/result.html', {'users': users})
