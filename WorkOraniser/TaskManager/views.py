from django.shortcuts import render
from .models import * 

# Create your views here.
def load_landingPage(request):
    if request.method == "POST":
        task_title = request.POST.get('title') 
        task_des = request.POST.get('des')
        task_time = request.POST.get('datetime')
        task_tag = request.POST.get('tag_sel')
        print(task_title,task_des,task_time,task_tag)
        task_instance = Tasks(Title = task_title,Description = task_des,Timeline = task_time,Tag = Tag.objects.get(Tg_name = task_tag))
        task_instance.save()

    # elif request.method == "GET":
    #     data = Tasks.objects.all()
    #     for i in data: 
    #         print(i.Title)
        
    return render(request,'landing.html',{
        'alltags': Tag.objects.all(),
        'alltasks': Tasks.objects.all()
    })
