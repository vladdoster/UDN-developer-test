from django.db import models


class Participant(models.Model):
    """
    Fields:
    - Participant Name
    - Participant Age
    - Does Participant have any siblings?
    - Known environmental exposures
    - Known genetic mutations

    After submitting information you should be redirected to the list view
    where each participant and the values they entered are present.
    """
    name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()
    has_siblings = models.BooleanField(default=False)

    # Add a dropdown box for each participant that would have 3 values
    # (Not Reviewed, Reviewed - Accepted, Reviewed - Not Accepted).
    # Changing of this dropdown should save this field alongside the participant data.

    NEED_REVIEW = 'NR'
    REVIEWED = 'RO'
    REVIEWED_ACCEPTED = 'RA'
    REVIEWED_NOT_ACCEPTED = 'RR'

    app_status = [
        (NEED_REVIEW, 'Needs review'),
        (REVIEWED, 'Reviewed - No decision made'),
        (REVIEWED_ACCEPTED, 'Reviewed - Accepted'),
        (REVIEWED_NOT_ACCEPTED, 'Reviewed - Not Accepted'),
    ]

    application_status = models.CharField(
        max_length=2,
        choices=app_status,
        default=NEED_REVIEW,
    )

    def app_status_verbose(self):
        return dict(Participant.app_status)[self.application_status]


class ParticipantEnvironmentalExposure(models.Model):
    participant = models.ForeignKey(Participant, models.CASCADE)
    envexposure = models.CharField(max_length=200)


class ParticipantGeneMutation(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    genemutation = models.CharField(max_length=200)
