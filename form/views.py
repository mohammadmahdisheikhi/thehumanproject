from django.shortcuts import render, redirect
from .forms import UserProfileForm, CustomUser, UserResponse
from django.http import JsonResponse
from register.models import Gender
from .models import FormPage

# Create your views here.

def index(request):

    concepts = ["عشق", "عدالت", "آزادی"]
    manifest = FormPage.objects.first()

    if request.method == 'POST':
        phone = request.POST.get('phone')
        text = request.POST.get('text')

        user = CustomUser.objects.filter(phone=phone).first()

        concept = request.POST.get('concept')  # ✅ Get the concept



        if not user:
            user = CustomUser.objects.create(
                phone=phone,
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                age=int(request.POST.get('age')),
                gender=int(request.POST.get('gender')),
                country=request.POST.get('country'),
                city=request.POST.get('city')
            )

        UserResponse.objects.create(
            user=user,
            concept=concept,         # ✅ Store the concept in DB
            text=request.POST.get('text')
        )

        return redirect('index')

    return render(request, 'form.html', {'manifest': manifest, 'concepts': concepts,})


def check_user_exists(request):
    phone = request.GET.get('phone')
    exists = CustomUser.objects.filter(phone=phone).exists()
    return JsonResponse({'exists': exists})

