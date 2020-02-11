from django.urls import path
from cc import views
app_name='cc'

urlpatterns = [
    path('',views.hello,name='hello')
]
