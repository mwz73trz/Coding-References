from django.shortcuts import render
from .models import Subject, Program
from .forms import SubjectForm, ProgramForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def get_subject_by_id(subject_id):
    return Subject.objects.get(id=subject_id)

@login_required
def get_subject_list(request):
    subjects = Subject.objects.filter(user=request.user)
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

def get_program_by_id(program_id):
    return Program.objects.get(id=program_id)

def get_program_list(request, subject_id):
    subject = get_subject_by_id(subject_id)
    programs = subject.programs.all()
    return render(request, 'blogs/program_list.html', {'subject': subject, 'programs': programs})

def get_program_detail(request, subject_id, program_id):
    subject = get_subject_by_id(subject_id)
    program = get_program_by_id(program_id)
    return render(request, 'blogs/program_detail.html', {'subject': subject, 'program': program})

def new_program(request, subject_id):
    subject = get_subject_by_id(subject_id)
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            program = form.save(commit=False)
            program.subject = subject
            program.save()
            return(get_program_list(request))
    else:
        form = ProgramForm()
    return render(request, 'blogs/program_form.html', {'form': form, 'type_of_request': 'New'})

def edit_program(request, subject_id, program_id):
    subject = get_subject_by_id(subject_id)
    program = get_program_by_id(program_id)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            program = form.save(commit=False)
            program.save()
            return(get_program_list(request))
    else:
        form = ProgramForm(instance=program)
    return render(request, 'blogs/program_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_program(request, subject_id, program_id):
    if request.method == 'POST':
        program = get_program_by_id(program_id)
        program.delete()
    return(get_program_list(request))

