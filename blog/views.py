from django.shortcuts import render
from .models import About, Experience, Education, Certificate, Skill, Project, Interest

def index(request):
    about = About.objects.first()  
    context = {
        "first_name": about.first_name,
        "last_name": about.last_name,
        "address": about.address,
        "phone": about.phone,
        "email": about.email,
        "linkedin": about.linkedin,
        "github": about.github,
        "about": about.about_text,

        "experiences": Experience.objects.all(),
        "education": Education.objects.all(),
        "certificates": Certificate.objects.all(),
        "skills": Skill.objects.all(),
        "projects": Project.objects.all(),
        "interests": Interest.objects.all(),
    }
    return render(request, "blog/index.html", context)
