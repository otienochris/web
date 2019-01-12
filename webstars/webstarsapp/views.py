from django.shortcuts import render
from datetime import datetime
# import for decorator missing

# Create your views here.

def home(request):
   

    return render(request, 'webstarsapp/index.html')



# @loginrequired
def profile(request):
    

    return render(request, 'webstarsapp/profile.html')
    pass
