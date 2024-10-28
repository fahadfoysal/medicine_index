from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Medicine
from .forms import MedicineForm, LoginForm, RegisterForm


# Medicine List & Search View
def medicine_list(request):
    medicines = Medicine.objects.all().order_by('-id')
    query = request.GET.get('q', '')
    if query:
        medicines = medicines.filter(Q(name__icontains=query) | Q(generic_name__icontains=query))

    context = {
        'medicines': medicines,
        'query': query,
    }
    return render(request, 'medicines/medicine_list.html', context)


@login_required(login_url='user_login') 
def medicine_create(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm()

    return render(request, 'medicines/medicine_form.html', {'form': form})


@login_required(login_url='user_login')  
def medicine_update(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)

    if request.method == 'POST':
        form = MedicineForm(request.POST or None, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm(instance=medicine)

    return render(request, 'medicines/medicine_form.html', {'form': form, 'medicine': medicine})


@login_required(login_url='user_login') 
def medicine_delete(request, pk):
    medicine = Medicine.objects.get(pk=pk)
    if request.method == 'POST':
        medicine.delete()
        return redirect('medicine_list')
    return render(request, 'medicines/medicine_confirm_delete.html', {'medicine': medicine})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = RegisterForm()
    return render(request, 'medicines/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('medicine_list')
    else:
        form = LoginForm()
    return render(request, 'medicines/login.html', {'form': form})


@login_required(login_url='user_login') 
def user_logout(request):
    logout(request)
    return redirect('user_login')
