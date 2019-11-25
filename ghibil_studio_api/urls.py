from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ghibli studio urls
    path('ghibli-movies/', include('movies.urls', namespace='ghibli-movies')),
]
