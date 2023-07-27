from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login_page,name='login'),
    path('signup/',views.signup,name='signup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('meeting/',views.videocall, name='meeting'),
    path('logout/',views.logout_page, name='logout'),
    path('join/',views.join_room, name='join_room'),

]