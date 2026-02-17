from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Стартовая страница каталога</h1>')

def info(request):
    return HttpResponse('<h1>Информация о каталоге</h1>')

def authors(request, Family, Name):
    return HttpResponse(f"""
    <h1>Известный автор</h1>
    <p>С фамилией {Family}</p>
    <p>И с именем {Name}</p>                    
    """)