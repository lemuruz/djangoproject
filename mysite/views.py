# from django.http import HttpResponse
from django.shortcuts import render
import time,os

# t = time.time()

def index(request):

    home_path = os.path.join(os.path.expanduser("~"))
    home_file = sorted(os.listdir(home_path))
    
    current_time = time.ctime(time.time())
    return render(request, 'note/menu.html',
                  {'current_time': current_time,
                   'paths' : home_file})
