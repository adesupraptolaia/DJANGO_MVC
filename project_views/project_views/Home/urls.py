from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('blog/', Blog),
    path('blog/input/', inputblog, name='inputblog'),
    path('mentor/', mentor),
    path('mentor/input/', inputmentor, name='inputmentor'),
    path('mentee/', mentee),
    path('mentee/input/', inputmentee, name='inputmentee'),
    path('author/', Author),

]