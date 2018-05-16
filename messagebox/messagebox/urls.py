from django.contrib import admin
from django.urls import path
from olxapp.views import conversations_list_view, answers_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', conversations_list_view),
    path('answers/', answers_list, name='answers_list'),

]