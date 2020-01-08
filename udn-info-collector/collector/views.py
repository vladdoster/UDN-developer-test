from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, UpdateView
from . import forms, models


class NewParticipantView(FormView):
    template_name = 'pages/index.html'
    form_class = forms.ParticipantForm
    success_url = '/participants/'

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


class ParticipantUpdateView(UpdateView):
    model = models.Participant
    fields = '__all__'
    # it should just use the suffix, but POC > elegant
    # template_name_suffix = '_update_form'
    template_name = 'pages/participant_update_form.html'

