import logging

from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from . import forms, models

# Get an instance of a logger
logger = logging.getLogger(__name__)


class NewParticipantView(FormView):
    template_name = 'pages/index.html'
    form_class = forms.ParticipantForm
    success_url = "/"

    def form_valid(self, form):
        form.clean()
        form.save()
        return super().form_valid(form)


class ParticipantListView(ListView):
    template_name = 'pages/participants.html'
    context_object_name = "participants_model_list"
    model = models.Participant
    queryset = models.Participant.objects.all()
    success_url = reverse_lazy('participants')
