from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.start_page,name='start_page'),
    path('signup/',views.signup,name='signup'),
    path('singin/',views.signin,name='singin'), 
]