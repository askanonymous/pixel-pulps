from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('home.urls')),  # Replace 'app_name' with your app's name
    path('median-salary/', include('home.urls'))  

]

