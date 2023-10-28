from django.urls import include,path
from . import views 

urlpatterns = [
    path('',views.load_landingPage,name="main_page"),
    path('delete/<task_id>',views.delete_task,name="delte_task"),
    path('post/<task_id>',views.postpond_task,name="postpond_task"),
    path('comp/<task_id>',views.complete_task,name="complete_task"),
    path('bargraph',views.get_bar_data,name="bar_graph"),
]