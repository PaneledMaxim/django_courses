from django.shortcuts import render
from django.http import HttpResponse
from .data import courses_data, authors_data

def index(request):
    return render(request, 'index.html')

def info(request):
    return render(request, 'info.html')


def authors(request):
    context = {'authors': authors_data}
    return render(request, 'authors.html', context)

def authors_details(request, author_id):
    author= None
    for a in authors_data:
        if a['id'] == author_id:
            author = a
            break
    
    if author:
        author_courses = []
        for c in courses_data:
            if c['author_id'] == author_id:
                author_courses.append(c)
        context = {
            'author': author,
            'author_courses': author_courses
        }
        return render(request, 'author_details.html', context)
    else:
        return render(request, 'not_found.html')
        


def courses(request):
    context = {'courses': courses_data}
    return render(request, 'courses.html', context)

def course_details(request, course_id):
    course = None
    for c in courses_data:
        if c['id'] == course_id:
            course = c
            break

    if course:
        author= None
        for a in authors_data:
            if a['id'] == course['author_id']:
                author = a
                break
        context= {
            'course': course,
            'author': author
        }
        return render(request, 'course_detail.html', context)
    else:
        return render(request, 'not_found.html')


def not_found(request, exception):
    return render(request, 'not_found.html')

        