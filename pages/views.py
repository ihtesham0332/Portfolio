from django.shortcuts import render
from .models import Project, Skill, Experience

def home_page_view(request):
    my_projects = Project.objects.all()
    my_skills = Skill.objects.all()
    my_experience = Experience.objects.all()
    
    context = {
        "projects": my_projects,
        "skills": my_skills,
        "experience": my_experience
    }
    return render(request, "home.html", context)


from django.shortcuts import render, get_object_or_404
# (Keep your existing home_page_view code here)

def project_detail_view(request, pk):
    # This fetches the single project, or shows a 404 error if it doesn't exist
    single_project = get_object_or_404(Project, pk=pk)
    
    return render(request, "project_detail.html", {"project": single_project})


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Using your email from the CV [cite: 3]
        user_email = "khanihtesham0332@gmail.com" 

        # The logic to send the email
        send_mail(
            subject=f"New Portfolio Message from {name}",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user_email],
            fail_silently=False,
        )
        return redirect('home') # Redirect after sending
        
    return render(request, "contact.html")


# pages/views.py
from django.shortcuts import render
from .models import Education  # Make sure your model is named Education

def education_view(request):
    # This fetches every education record you added in the admin panel
    items = Education.objects.all().order_by('-degree') 
    return render(request, "education.html", {"education_items": items})

def services_view(request):
    return render(request, "services.html")

def about_view(request):
    return render(request, "about.html")