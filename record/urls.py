from django.urls import path
from record.views import *

urlpatterns = [
    path("query-builder", query_builder , name="query-builder"),
    path("upload-data", upload_data , name="upload-data"),
    path('api/record-count/', RecordCountView.as_view(), name='record-count'),

]