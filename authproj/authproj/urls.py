from django.contrib import admin
from django.urls import path,include
from myapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view),
    path('java/',java_view),
    path('python/',python_view),
    path('aptitude/',aptitude_view),
    path('logout/',logout_view),
    path('signup/',signup_view),
    path('accounts/',include('django.contrib.auth.urls'))
]
