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
        - START_DATETIME, RELEASE_INTERVAL and MARK_INTERVAL are set in the
          main settings file
        - times are in the timezone TIME_ZONE, set in the main settings file
        - returned release number is a decimal (ie. 1.5) if current datetime is
          within the mark_interval

    Test:
        - before start date (pass)
        - at start date (pass)
        - after start date but before start date + interval (pass)
        - at start date + interval (pass)
        - after start date + interval (pass)

    :return: int
    """

    release_interval = timedelta(days=int(settings.RELEASE_INTERVAL))

    mark_interval = timedelta(days=int(settings.MARK_INTERVAL))

    start = timezone.make_aware(datetime.strptime(settings.START_DATETIME,
            settings.DATETIME_FORMAT), timezone.get_default_timezone())

    current = timezone.localtime(timezone.now(),
                                 timezone.get_default_timezone())

    release = 0

    mark = 0

    date_time = start

    while date_time <= current:
        release += 1
        date_time += release_interval
        if date_time <= current:
            mark += 1
        date_time += mark_interval

    if release != mark:
        return release
    return release + 0.5
