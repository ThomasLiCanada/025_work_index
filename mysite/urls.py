# project urls.py

from django.contrib import admin
from django.urls import path, include
from websites.views import *  # * means all views
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static


def home(request):
    return HttpResponse('Hello! Home page.')  # show hello on home page
    # return render(request, 'urls_list.html', {})  # templates/urls_list.html


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),

    path('desktop/', desktop_view, name='desktop_view'),
    path('update_order/', update_order, name='update_order'),

    path('', desktop_view, name='desktop'), # as homepage
    path('input_index/', input_index_view, name='input_index'),
    path('delete_index/<str:pk>', delete_index, name='delete_index'),
    path('desktop_view_for_delete_icon/', desktop_view_for_delete_icon, name='desktop_view_for_delete_icon'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

