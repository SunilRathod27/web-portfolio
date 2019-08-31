from django.contrib.auth.models import User
from django.shortcuts import render
from .models import (Certification, Education, Focus, ProfessionalSkill,
                     Profile, Project, ProjectCategory, Recommendation,
                     Seminar, TechnicalSkill, WorkExperience)


def home(request):
    seej = User.objects.get(id=1)
    top_skills = TechnicalSkill.objects.filter(is_top_skill=True)
    focus = Focus.objects.filter(is_active=True)
    technical_skills = TechnicalSkill.objects.order_by('name')
    professional_skills = ProfessionalSkill.objects.order_by('name')
    education = Education.objects.order_by('-id')
    work_experience = WorkExperience.objects.order_by('-id')
    categories = ProjectCategory.objects.order_by('name')
    projects = Project.objects.order_by('title')
    certs = Certification.objects.order_by('-id')
    seminars = Seminar.objects.order_by('-id')
    recommendations = Recommendation.objects.order_by('id')

    context = {
        'seej': seej,
        'top_skills': top_skills,
        'focus': focus,
        'technical_skills': technical_skills,
        'professional_skills': professional_skills,
        'education': education,
        'work_experience': work_experience,
        'categories': categories,
        'projects': projects,
        'certs': certs,
        'seminars': seminars,
        'recommendations': recommendations
    }
    return render(request, 'contents/portfolio.html', context)
