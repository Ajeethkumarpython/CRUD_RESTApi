from django.urls import path, include
from . import views
from .router import router

urlpatterns = [
    path('', views.index, name=''),
    path('api/', include(router.urls))
]