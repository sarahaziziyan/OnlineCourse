from django.contrib import admin
from django.urls import path
from OnlineCourseApp.views import *

urlpatterns = [
    path('', login),
    path('admin', admin.site.urls),
    path('sign_up', sign_up, name='sign_up'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('edit_profile', edit_profile, name='edit_profile'),
    path('update_profile_data', update_profile_data, name='update_profile_data'),
]

from . import settings
from django.contrib.staticfiles.urls import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

