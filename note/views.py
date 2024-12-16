from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import note
from django.template import loader

def index(request):
    all_note = note.objects.order_by("-Pub_Date")[:5]
    template = loader.get_template("note/index.html")
    # output = "\n".join([q.Title for q in all_note])
    context = { 
        "all_note" : all_note,
    }
    return HttpResponse(template.render(context,request))
def detail(request,note_id):
    note_instance = get_object_or_404(note, pk=note_id)
    
    return render(request,"note/note_content.html",{"note_instance": note_instance,
                                                    "Pub_date": note_instance.Pub_Date})
    