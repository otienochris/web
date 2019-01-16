from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.models import User
# import for decorator missing

# Create your views here.

def home(request):
   

    return render(request, 'webstarsapp/index.html')



# @login_required()
# def profile(request):
#     return render(request, 'webstarsapp/profile.html', {})


