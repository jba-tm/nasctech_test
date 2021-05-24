from django.urls import path, include

from backend.apps.test_app.api.views import DataAPIView

app_name='api'
urlpatterns = [
    path('data/', DataAPIView.as_view(), name='data')
]