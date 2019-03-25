from django.shortcuts import render
from . import models

def index(request):
    num_book = models.Book.objects.all().count()
    num_instances = models.BookInstance.objects.all().count()
    num_instances_available = models.BookInstance.objects.filter(status = 'a').count()
    num_author = models.Author.objects.all().count()
    return render(request,
    'catalog/index.html',
     context={'num_book' : num_book , 'num_instances' : num_instances , 'num_instances_available' : num_instances_available , 'num_author' : num_author}
    )
