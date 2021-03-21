from django.shortcuts import render
from django.shortcuts import redirect
from .models import Categories
from .models import Task_Models
from .filters import TaskSearchParametr
from .forms import LoginForms, RegisterForms, Create
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def create(request):
    if request.method == "POST":
        form = Create(request.POST)
        form.save()
        return redirect('/task')
    form = Create
    context = {
        'form': form
    }
    return render(request, 'create_task.html', context)


def registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = RegisterForms()
        if request.method == 'POST':
            form = RegisterForms(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Новый пользователь был создан ' + user)
                return redirect('/login')

        context = {
            'form': form
        }
    return render(request, 'users/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')


def user_login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')

    else:
        form = LoginForms()

    return render(request, 'users/login.html', {'form': form})


def task_more_detailed(request, pk_test):
    ids = Task_Models.objects.get(id=pk_test)
    context = {

        'ids': ids
    }
    return render(request, 'task_details.html', context)


# Create your views here.
def task(request):
    form = Task_Models.objects.all()
    filters = TaskSearchParametr(request.GET, queryset=form)
    form = filters.qs
    context = {
        "form": form,
        'filters': filters

    }
    return render(request, 'task.html', context)


def main_menu(request):
    model = Categories.objects.all()

    context = {
        'model': model
    }

    return render(request, 'menu.html', context)


def test(request):
    form = Task_Models.objects.all()
    filters = ProductFilter(request.GET, queryset=form)
    form = filters.qs

    context = {
        "form": form,
        'filter': filters
    }

    return render(request, 'test.html', context)
