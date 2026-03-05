from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Teacher, TeacherInfo, Course, Student, StudentCourse

def index(request):
    teachers = Teacher.objects.all()
    return render (request, 'schedule/index.html', {'teachers': teachers})

def teacher_create(request):
    if request.method == 'POST':
        Teacher.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
        )
        return redirect('schedule_index')
    return render (request, 'schedule/teacher_create.html')

def teacher_update(request, teacher_id):
    teacher= Teacher.objects.get(id=teacher_id)
    if request.method == 'POST':
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.email = request.POST.get('email')
        teacher.save()
        return redirect('schedule_index')
    return render (request, 'schedule/teacher_update.html', {'teacher': teacher})

def teacher_delete(request, teacher_id):
    teacher= Teacher.objects.get(id=teacher_id)
    teacher.delete()
    return redirect('schedule_index')

def teacher_info(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    teacher_info = TeacherInfo.objects.filter(teacher_id=teacher_id).first()
    return render(request, 'schedule/teacher_info.html', {'teacher': teacher, 'teacher_info': teacher_info})

def teacher_info_update(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    teacher_info, _ = TeacherInfo.objects.get_or_create(teacher=teacher)

    if request.method == 'POST':
        teacher_info.phone = request.POST.get('phone', '')
        teacher_info.bio = request.POST.get('bio', '')
        teacher_info.experience_years = request.POST.get('experience_years', '')

        teacher_info.save()
        return redirect('teacher_info', teacher_id=teacher_id)
    return render (request, 'schedule/teacher_info_update.html', {'teacher_info': teacher_info})




def courses(request):
    teacher_id = request.GET.get('teacher_id')
    if teacher_id:
        courses = Course.objects.filter(teacher_id=teacher_id)
    else:
        courses = Course.objects.all()
    
    teachers = Teacher.objects.all()
    
    return render(request, 'schedule/courses.html', {
        'courses': courses,
        'teachers': teachers,
        'selected_teacher': teacher_id
    })

def create_course(request):
    if request.method == 'POST':
        Course.objects.create(
            title=request.POST['title'],
            description=request.POST.get('description', ''),
            teacher_id=request.POST['teacher_id']
        )
        return redirect('courses')
    teachers = Teacher.objects.all()
    return render(request, 'schedule/create_course.html', {'teachers': teachers})

def update_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        course.title = request.POST.get('title')
        course.description = request.POST.get('description')
        course.teacher_id = request.POST.get('teacher_id')
        course.save()
        return redirect('courses')
    teachers = Teacher.objects.all()
    return render(request, 'schedule/update_course.html', {'course': course, 'teachers': teachers})

def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('courses')

def student_index(request):
    students = Student.objects.all()
    return render(request, 'schedule/student_index.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        Student.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            birth_date=request.POST['birth_date'],
        )
        return redirect('student_index')
    return render (request, 'schedule/student_create.html')

def student_update(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.email = request.POST.get('email')
        student.birth_date = request.POST.get('birth_date')
        student.save()
        return redirect('student_index')
    return render (request, 'schedule/student_update.html', {'student': student})

def student_delete(request, student_id):
    student= Student.objects.get(id=student_id)
    student.delete()
    return redirect('student_index')

def student_enroll(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course = Course.objects.get(id=course_id)
        
        if not StudentCourse.objects.filter(student=student, course=course).exists():
            StudentCourse.objects.create(student=student, course=course)
        
        return redirect('student_courses', student_id=student_id)
    
    courses = Course.objects.all()
    return render(request, 'schedule/student_enroll.html', {'student': student, 'courses': courses})

def student_unenroll(request, student_id, course_id):
    student = Student.objects.get(id=student_id)
    course = Course.objects.get(id=course_id)
    
    StudentCourse.objects.filter(student=student, course=course).delete()
    
    return redirect('student_courses', student_id=student_id)

def student_courses(request, student_id):
    student = Student.objects.get(id=student_id)
    student_courses = StudentCourse.objects.filter(student=student)
    
    courses = [sc.course for sc in student_courses]
    
    return render(request, 'schedule/student_course.html', {
        'student': student,
        'courses': courses,
        'student_courses': student_courses,
    })
