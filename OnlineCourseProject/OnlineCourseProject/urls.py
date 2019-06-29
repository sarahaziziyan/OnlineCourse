from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from OnlineCourseApp.views import *

urlpatterns = [
    path('', myLogin),
    path('admin', admin.site.urls),
    path('admin/', admin.site.urls),
    path('sign_up', sign_up, name='sign_up'),
    path('login', myLogin, name='login'),
    path('logout', logout, name='logout'),
    path('edit_profile', edit_profile, name='edit_profile'),
    path('update_profile_data', update_profile_data, name='update_profile_data'),
    path('search_courses', search_courses, name ='search_courses'),
    path('my_courses', my_courses, name ='my_courses'),
    path('edit_profile', edit_profile, name ='edit_profile'),
    path('bootstrapDemo', bootstrapDemo),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)