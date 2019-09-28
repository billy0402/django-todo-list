from django.urls import path

from .views import root, request_test, render_test, homework

urlpatterns = [
    path('', root),
    path('request_test/', request_test),
    path('render_test/<int:n1>/<int:n2>/', render_test),
    path('homework/<int:start>/<int:stop>/<int:base>/', homework),
]
