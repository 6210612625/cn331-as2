from django.urls import path, include
from . import views 
app_name = "courses"
urlpatterns = [
    
    path('',views.index,name="index"),
    path('<int:course_id>',views.course,name= "course"),
    path('<int:course_id>/book',views.book,name="book"),
    
    ]