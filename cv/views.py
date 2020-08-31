from django.shortcuts import render
from .models import ContactDetail
from .models import Institution
from .models import Qualification
from .models import Skill
from .models import Experience

# Create your views here.


def cv(request):
    contact_details = ContactDetail.objects.all()
    institutions = Institution.objects.all().order_by("-end_date")
    qualifications = Qualification.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()

    return render(request, 'cv/cv.html', {
        "contact_details": contact_details,
        "institutions": institutions,
        "qualifications": qualifications,
        "skills": skills,
        "experiences": experiences,
    })
