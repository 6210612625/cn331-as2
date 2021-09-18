from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django import forms


# Create your views here.
from .models import *


def index(request):
    return render(request, "courses/index.html", {
        "courses": Course.objects.all(),

    })


def course(request, course_id):

    coursed = get_object_or_404(Course, pk=course_id)

    return render(request, "courses/courses.html", {
        "coursed": coursed,
        "students": coursed.student.all(),

    })

def book(request, course_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    coursed = get_object_or_404(Course, pk=course_id)

    students= coursed.student.all()
    num = coursed.quota
    if request.user not in coursed.student.all() :
        coursed.student.add(request.user)
    return HttpResponseRedirect(reverse("courses:course",args=[course_id]))

def remove(request, course_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))

    coursed = get_object_or_404(Course, pk=course_id)
    students = coursed.student.all()
    if request.user in coursed.student.all():
        coursed.student.remove(request.user)
    return HttpResponseRedirect(reverse("courses:index"))


