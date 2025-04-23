from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.urls import path, reverse
from .models import Employee
from .forms import UserCreateForm

def index(request):
    latest_employee_list = Employee.objects.order_by("-created_at")[:10]
    context = {
        "latest_employee_list": latest_employee_list,
    }
    return render(request, "userdoc/index.html", context)

def userWelcome(request, slug):
    employee = get_object_or_404(Employee, slug=slug)
    return render(request, "userdoc/user_welcome.html", {"employee": employee})

def new(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            # Save the new user to the database
            new_employee = form.save()
            return redirect(reverse('userdoc:userWelcome', args=[new_employee.slug]))
        else:
            # Handle form errors
            return render(request, "userdoc/user_create.html", {"form": form})
    else:
        form = UserCreateForm()
        # Render the user creation form
        return render(request, "userdoc/user_create.html", {"form": form})