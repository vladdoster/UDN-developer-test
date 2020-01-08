from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class VisualizerConfig(AppConfig):
    name = "udn-info-collector.collector"
    verbose_name = _("collector")
