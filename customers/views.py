from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CustomerForm
from .models import Customer
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('customers')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'User already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })

@login_required
def customers(request):
    customers = Customer.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'customers.html', {'customers': customers})

@login_required
def create_customer(request):
    if request.method == 'GET':
        return render(request, 'create_customer.html', {
            'form': CustomerForm
        })
    else:
        try:
            form = CustomerForm(request.POST)
            new_customer = form.save(commit=False)
            new_customer.user = request.user
            new_customer.save()
            return redirect('customers')
        except ValueError:
            return render(request, 'create_customer.html', {
                'form': CustomerForm,
                'error': 'Please provide valid data'
            })

@login_required
def customer_detail(request, customer_id):
    if request.method == 'GET':
        customer = get_object_or_404(Customer, pk=customer_id, user=request.user)
        form = CustomerForm(instance=customer)
        return render(request, 'customer_detail.html', {
            'customer': customer,
            'form': form
        })
    else:
        try:
            customer = get_object_or_404(Customer, pk=customer_id, user=request.user)
            form = CustomerForm(request.POST, instance=customer)
            form.save()
            return redirect('customers')
        except ValueError:
            return render(request, 'customer_detail.html', {'customer': customer, 'form': form, 'error': 'Error updating customer'})

@login_required
def complete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id, user=request.user)
    if request.method == 'POST':
        customer.datecompleted = timezone.now()
        customer.save()
        return redirect('customers')

@login_required
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id, user=request.user)
    if request.method == 'POST':
        customer.delete()
        return redirect('customers')

@login_required
def customers_completed(request):
    customers = Customer.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'customers.html', {'customers': customers})

@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('customers')
