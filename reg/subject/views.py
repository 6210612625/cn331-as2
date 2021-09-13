
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django import forms
# Create your views here.
from .models import Subject
def index(request):
    return render(request, "subject/index.html",{"subject": Subject.objects.all()
    })
def subject(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)

    return render(request, "subject/subject.html", {
        "subject": subject,
        "student": subject.student.all()
    })

'''
def register(request, subject_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login")
        return HttpResponseRedirect(reverse("users:login")+f"?next={request.path}")

    subject = get_object_or_404(Subject, pk=subject_id)
    if request.user not in subject.student.all():
        subject.student.add(request.user)
    return HttpResponseRedirect(reverse("subject:subject", args=(subject_id,)))


class NewTaskForm(forms.Form):
    task = forms.CharField(label='New Task', min_length=8)

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session['tasks'] += [task]
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, 'tasks/subject.html', { 'form': form })

    return render(request, 'tasks/subject.html', { 'form': NewTaskForm })
    '''