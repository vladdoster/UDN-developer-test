from django.contrib import admin

from .models import Participant, ParticipantEnvironmentalExposure, ParticipantGeneMutation


class EnvironmentalExposuresInline(admin.TabularInline):
    model = ParticipantEnvironmentalExposure


class GeneMutationInline(admin.TabularInline):
    model = ParticipantGeneMutation


class ParticipantModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'has_siblings', 'application_status']
    inlines = [
        EnvironmentalExposuresInline,
        GeneMutationInline,
    ]


class EnvironmentalExposuresModelAdmin(admin.ModelAdmin):
    list_display = ['envexposure']


class GeneMutationModelAdmin(admin.ModelAdmin):
    list_display = ['genemutation']


admin.site.register(Participant, ParticipantModelAdmin)
admin.site.register(ParticipantEnvironmentalExposure, EnvironmentalExposuresModelAdmin)
admin.site.register(ParticipantGeneMutation, GeneMutationModelAdmin)
