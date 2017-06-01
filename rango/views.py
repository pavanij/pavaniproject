from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category

#def index(request):
#    return HttpResponse("Rango says hey there partner!")# Create your views here.
def about(request):
    return render(request, 'rango/about.html')
def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    #return render(request, 'rango/index.html', context=context_dict)
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)
