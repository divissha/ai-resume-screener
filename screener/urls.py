from django.urls import path
from .views import upload_resume
from . import views

urlpatterns = [
    path('', upload_resume, name='upload_resume'),

    path(
    "download/",
    views.download_report,
    name="download"),

    path(
    "history/",
    views.history,
    name="history"),
]