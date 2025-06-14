from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume
from .forms import ResumeForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

def home(request):
    return render(request, 'resumes/home.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'resumes/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'resumes/login.html', {'error': 'Invalid credentials'})
    return render(request, 'resumes/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    resumes = Resume.objects.filter(user=request.user)
    return render(request, 'resumes/dashboard.html', {'resumes': resumes})

@login_required
def resume_create(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('dashboard')
    else:
        form = ResumeForm()
    return render(request, 'resumes/resume_form.html', {'form': form, 'title': 'Create Resume'})

@login_required
def resume_edit(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ResumeForm(instance=resume)
    return render(request, 'resumes/resume_form.html', {'form': form, 'title': 'Edit Resume'})

@login_required
def resume_delete(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    if request.method == 'POST':
        resume.delete()
        return redirect('dashboard')
    return render(request, 'resumes/resume_confirm_delete.html', {'resume': resume})

@login_required
def resume_detail(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    return render(request, 'resumes/resume_detail.html', {'resume': resume})

@login_required
def resume_pdf(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    html_string = render_to_string('resumes/resume_pdf.html', {'resume': resume})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="resume_{resume.id}.pdf"'
    weasyprint.HTML(string=html_string).write_pdf(response)
    return response