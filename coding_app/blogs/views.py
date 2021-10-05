from django.shortcuts import render
from .models import Subject
from .forms import SubjectForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def get_subject_by_id(subject_id):
    return Subject.objects.get(id=subject_id)

@login_required
def get_subject_list(request):
    subjects = Subject.objects.filter(user=request.user)
    print(subjects)
    return render(request, 'blogs/subject_list.html', {'subjects': subjects})

def get_subject_detail(request, subject_id):
    subject = get_subject_by_id(subject_id)
    return render(request, 'blogs/subject_detail.html', {'subject': subject})

def new_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            return (get_subject_list(request))
    else:
        form = SubjectForm()
    return render(request, 'blogs/subject_form.html', {'form': form, 'type_of_request': 'New'})

def edit_subject(request, subject_id):
    subject = get_subject_by_id(subject_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            return get_subject_list(request)
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'blogs/subject_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_subject(request, subject_id):
    if request.method == 'POST':
        subject = get_subject_by_id(subject_id)
        subject.delete()
    return get_subject_list(request)
