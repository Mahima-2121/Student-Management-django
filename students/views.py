from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Student
from .forms import StudentForm


def student_list(request):
    query  = request.GET.get('q', '')
    course = request.GET.get('course', '')
    students = Student.objects.all().order_by('first_name')
    if query:
        students = students.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)  |
            Q(roll_number__icontains=query)|
            Q(email__icontains=query)
        )
    if course:
        students = students.filter(course=course)
    courses = Student.objects.values_list(
                'course', flat=True).distinct()
    return render(request, 'students/list.html', {
        'students': students,
        'query': query,
        'courses': courses,
        'selected_course': course,
    })

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request,
        'students/detail.html', {'student': student})


def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Student added!')
        return redirect('student_list')
    return render(request, 'students/form.html',
        {'form': form, 'action': 'Add Student'})


def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None,
                       instance=student)
    if form.is_valid():
        form.save()
        messages.success(request, 'Student updated!')
        return redirect('student_detail', pk=pk)
    return render(request, 'students/form.html',
        {'form': form, 'action': 'Edit Student'})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted.')
        return redirect('student_list')
    return render(request,
        'students/confirm_delete.html',
        {'student': student})