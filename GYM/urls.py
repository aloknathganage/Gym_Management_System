from django.urls import path
from . import views
urlpatterns = [
    path('',views.Login,name='login'),
    path('index',views.Index,name='index'),
    path('logout/',views.Logout, name='logout'),

    path('add_member/',views.Add_member, name='add_member'),
    path('view_member/',views.View_member, name='view_member'),
    path('delete_member(?p<int:pid>',views.Delete_Member, name='delete_member'),

    path('add_plan/',views.Add_plan, name='add_plan'),
    path('view_plan/',views.View_plan, name='view_plan'),
    path('delete_plan(?p<int:pid>)',views.Delete_plan, name='delete_plan'),

    path('add_equipment/',views.Add_equipment, name='add_equipment'),
]