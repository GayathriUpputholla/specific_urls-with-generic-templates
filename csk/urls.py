from django.urls import path
from csk.views import*
app_name='anything'
urlpatterns=[
    path('siri/',siri,name='siri'),
]