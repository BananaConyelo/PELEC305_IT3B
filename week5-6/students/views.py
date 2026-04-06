from django.shortcuts import render, redirect
from .forms import StudentForm

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_create')
    else:
        form = StudentForm()
    
    return render(request, 'student_form.html', {'form' : form})
