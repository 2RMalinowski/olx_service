from django.contrib import admin
from django.urls import path
from olxapp.views import conversations_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', conversations_list_view),

]