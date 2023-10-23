from django.shortcuts import render,redirect
from .models import * 
from django.utils import timezone
from datetime import timedelta

# Create your views here.
def load_landingPage(request):
    if request.method == "POST":
        task_title = request.POST.get('title') 
        task_des = request.POST.get('des')
        task_time = request.POST.get('datetime')
        task_tag = request.POST.get('tag_sel')
        # if task_time < timezone.now():
        #     task_status = 'lt'
        task_instance = Tasks(Title = task_title,Description = task_des,Timeline = task_time,Tag = Tag.objects.get(Tg_name = task_tag))
        task_instance.save()
        return redirect('main_page')

    elif request.method == "GET":
        data = Tasks.objects.all()
        for i in data: 
            if i.Timeline < timezone.now():
                i.Status = 'lt'
                i.save()
        
    return render(request,'landing.html',{
        'alltags': Tag.objects.all(),
        'alltasks': Tasks.objects.all()
    })


def delete_task(request,task_id):
    inst = Tasks.objects.get(id = task_id)
    inst.Status = 'dt'
    inst.save()
    return redirect('main_page')

def postpond_task(request,task_id):
    inst = Tasks.objects.get(id = task_id)
    inst.Timeline = inst.Timeline + timedelta(days=1)
    inst.Status = 'ot' 
    inst.save()
    return redirect('main_page')

def complete_task(request,task_id):
    inst = Tasks.objects.get(id = task_id)
    inst.Is_completed = True 
    inst.save()
    return redirect('main_page')