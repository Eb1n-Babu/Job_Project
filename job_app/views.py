from django.http import HttpResponse
from django.shortcuts import render
from .models import  Job

from django.shortcuts import render
from .models import Job

def Home(request):
    message = ""

    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")

        if Job.objects.filter(name=name, age=age, phone_number=phone_number, email=email).exists():
            message = "⚠️ Record already exists"
        else:
            Job.objects.create(name=name, age=age, phone_number=phone_number, email=email)
            message = "✅ Successfully applied! Our team will contact you soon."

    return render(request, "home.html", {"message": message})
