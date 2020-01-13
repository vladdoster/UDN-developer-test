from django.urls import path

from .views import NewParticipantView, ParticipantListView

app_name = "collector"
urlpatterns = [
    path("", ParticipantListView.as_view(), name='participants'),
    path("new_participant/", NewParticipantView.as_view(), name='new_participant'),
]
