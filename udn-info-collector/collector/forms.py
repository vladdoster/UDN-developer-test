# import the logging library
import logging

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, HTML, Div
from django import forms

from . import models

# Get an instance of a logger
logger = logging.getLogger(__name__)


class ParticipantForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        envexposures = models.ParticipantEnvironmentalExposure.objects.filter(
            participant=self.instance
        )
        genemutations = models.ParticipantGeneMutation.objects.filter(
            participant=self.instance
        )

        # This can be reduced, i am doing a POC. Very easy to yank in vim and replace all
        #################################################
        for i in range(len(envexposures) + 1):
            field_name = 'envexposure_%s' % (i,)
            self.fields[field_name] = forms.CharField(required=False, widget=forms.Textarea)
            try:
                self.initial[field_name] = envexposures[i].envexposure
            except IndexError:
                self.initial[field_name] = ''

        for i in range(len(genemutations) + 1):
            field_name = 'genemutation_%s' % (i,)
            self.fields[field_name] = forms.CharField(required=False, widget=forms.Textarea)
            try:
                self.initial[field_name] = genemutations[i].genemutation
            except IndexError:
                self.initial[field_name] = ''
        #################################################

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('name', ),
                Field('age', ),
                'has_siblings',
                'application_status',
                HTML("""<button onclick="newInput('environmentexposures')" style="margin-bottom: 5px;" type="button"
                                  class="btn btn-success btn-sm"><span class="fas fa-plus pull-left"></span> Add environment exposure
                          </button>"""),
                Div(Field('envexposure_0', rows=2, cols=2), css_class="environmentexposures", ),
                HTML("""<button onclick="newInput('geneticmodifications')" style="margin-bottom: 5px;" type="button"
                                                  class="btn btn-success btn-sm"><span class="fas fa-plus pull-left"></span> Add genetic modification
                                          </button>"""),
                Div(Field('genemutation_0', rows=2, cols=2), css_class="geneticmodifications", ),
            ),
            ButtonHolder(
                Submit('submit', 'Submit participant data')
            )
        )

    def clean(self):
        # This can be reduced, i am doing a POC. Very easy to yank in vim and replace all
        #################################################
        envexposures = set()
        i = 0
        field_name = 'envexposure_%s' % (i,)
        while self.cleaned_data.get(field_name):
            envexposure = self.cleaned_data[field_name]
            if envexposure in envexposures:
                self.add_error(field_name, 'Duplicate')
            else:
                envexposures.add(envexposure)
            i += 1
            field_name = 'envexposure_%s' % (i,)
        self.cleaned_data['envexposures'] = envexposures

        genemutations = set()
        i = 0
        field_name = 'genemutation_%s' % (i,)
        while self.cleaned_data.get(field_name):
            genemutation = self.cleaned_data[field_name]
            if genemutation in genemutations:
                self.add_error(field_name, 'Duplicate')
            else:
                genemutations.add(genemutation)
            i += 1
            field_name = 'genemutation_%s' % (i,)
        self.cleaned_data['genemutations'] = genemutations
        #################################################

    def get_envexposure_fields(self):
        for field_name in self.fields:
            if field_name.startswith('envexposure_'):
                yield self[field_name]

    def get_genemodification_fields(self):
        for field_name in self.fields:
            if field_name.startswith('genemutation_'):
                yield self[field_name]

    def save(self):
        participant = super(ParticipantForm, self).save(commit=False)
        participant.name = self.cleaned_data['name']
        participant.age = self.cleaned_data['age']
        participant.has_siblings = self.cleaned_data['has_siblings']
        # Must save first in newer Django versions
        participant.save()
        # This can be reduced, i am doing a POC. Very easy to yank in vim and replace all
        #################################################
        for envexposure in self.cleaned_data['envexposures']:
            logger.debug(envexposure)
            models.ParticipantEnvironmentalExposure.objects.create(
                participant=participant,
                envexposure=envexposure,
            )
        for genemutation in self.cleaned_data['genemutations']:
            models.ParticipantGeneMutation.objects.create(
                participant=participant,
                genemutation=genemutation,
            )
        #################################################

    class Meta:
        model = models.Participant
        fields = '__all__'
