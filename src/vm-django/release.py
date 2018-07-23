"""
Functions used to handle mystery clue release.
"""

from django.utils import timezone
from datetime import datetime, timedelta
from django.conf import settings


def get_current_release():
    """
    Returns the current release number, otherwise returns zero if
    START_DATETIME not yet reached.

    Note:
        - START_DATETIME and RELEASE_INTERVAL are set in the main settings file
        - times are in the timezone TIME_ZONE, set in the main settings file

    Test:
        - before start date (pass)
        - at start date (pass)
        - after start date but before start date + interval (pass)
        - at start date + interval (pass)
        - after start date + interval (pass)

    :return: int
    """
    release = 0

    interval = timedelta(days=int(settings.RELEASE_INTERVAL))

    start = timezone.make_aware(datetime.strptime(settings.START_DATETIME,
            settings.DATETIME_FORMAT), timezone.get_default_timezone())

    current = timezone.localtime(timezone.now(),
                                 timezone.get_default_timezone())

    while start + release*interval <= current:
        release += 1

    return release
