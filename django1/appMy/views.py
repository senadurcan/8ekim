from django.shortcuts import render
from appMy.models import Construction
# Create your views here.




def index(request):
    projeler = Construction.objects.all()
    
    
    context = {
            "projeler":projeler,
    }
    return render(request, 'index.html', context)