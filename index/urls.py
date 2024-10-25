from django.urls import path
from index.views import LoadFileView

app_name = "index"
urlpatterns = [
    path("", LoadFileView.as_view(), name="upload-file"),
]
