from django.shortcuts import render
from app_core.models import About,Introduction
from app_core.models import Certification, Education
from app_core.models import Employment, EmploymentPosition
from app_core.models import Skill, Skill_Set, Skill_Desc
from app_core.models import Quote, Testimonial

import logging
from django.http import HttpResponse

# Create your views here.

def index(request):
    About_first = About.objects.first()
    Introductions = Introduction.objects.all()
    Skills = Skill.objects.all()
    Skill_Sets = Skill_Set.objects.all()
    Skill_Descs = Skill_Desc.objects.all()
    Certifications = Certification.objects.all()
    Employments = Employment.objects.all().order_by('-start')
    EmploymentPositions = EmploymentPosition.objects.all().order_by('-start')
    Educations = Education.objects.all()
    Quotes = Quote.objects.all()
    Testimonials = Testimonial.objects.all()
    context = {
        'About_first': About_first,
        'Introductions': Introductions,
        'Skills': Skills,
        'Skill_Sets': Skill_Sets,
        'Skill_Descs': Skill_Descs,
        'Certifications': Certifications,
        'Employments': Employments,
        'EmploymentPositions': EmploymentPositions,
        'Educations': Educations,
        'Quotes': Quotes,
        'Testimonials': Testimonials,
    }
    return render(request, 'index.html', context)

# initialize logger to get logging and console output
logger = logging.getLogger(__name__)

def cookie_read(request):
    logger.error(request.COOKIES.get('TEST'))
    respo = HttpResponse(request.COOKIES.get('TEST'))
    return respo

def cookie_write(request, cookie_val):
    respo = HttpResponse('Cookie set!')
    respo.set_cookie('TEST', cookie_val)
    return respo

def get_info(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    logger.error(ip)
    return HttpResponse('Done!')