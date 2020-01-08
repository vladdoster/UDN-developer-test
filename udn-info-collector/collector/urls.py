from django.urls import path
from .views import NewParticipantView, ParticipantListView, ParticipantUpdateView

app_name = "collector"
urlpatterns = [
    path("", NewParticipantView.as_view(), name='new_participant'),
    path("participants/", ParticipantListView.as_view(), name='participants'),
    path("participant/<int:pk>/", ParticipantUpdateView.as_view(), name='update_participant'),
]
