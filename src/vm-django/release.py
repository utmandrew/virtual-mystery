"""
Functions used to handle mystery clue release.
"""

from django.utils import timezone
from datetime import datetime, timedelta
from django.conf import settings


def get_interval(interval):
    """
    * Helper Function *

    Returns a timedelta object of, interval, days.

    :param interval: string
    :return: timedelta object
    """

    return timedelta(days=int(interval))


def get_datetime(dt):
    """
    * Helper Function *

    Returns a time zone, TIME_ZONE, aware datetime object from the string,
    dt, in the format, DATETIME_FORMAT.

    NOTES:
     - TIME_ZONE and DATETIME_FORMAT are set in the main settings file

    :param dt: string
    :return: datetime object
    """

    return timezone.make_aware(datetime.strptime(dt, settings.DATETIME_FORMAT),
                               timezone.get_default_timezone())


def get_current_datetime():
    """
    * Helper Function *

    Returns a timezone aware datetime object of the current datetime.

    Note:
     - TIME_ZONE is set in the main settings file

    :return: datetime object
    """

    return timezone.localtime(timezone.now(), timezone.get_default_timezone())


def get_current_release():
    """
    Returns a tuple consisting of three positions:

        0 - current release number

            Returns the current release number, otherwise returns zero if
            START_DATETIME was not yet reached. If the mystery has ended
            (ie. END_DATETIME was reached), returns the number of the last
            legal release.

        1 - mark flag

            Returns True iff the current datetime is within a marking interval.
            Otherwise, returns False.

        2 - mystery_end flag

            Returns True iff the current datetime has reached the END_DATETIME
            mystery deadline. Otherwise returns False.

    Note:
        - START_DATETIME, RELEASE_INTERVAL, MARK_INTERVAL and END_DATETIME are
          set in the main settings file

    Test:
        - before start date (pass)
        - at start date (pass)
        - after start date but before start date + interval (pass)
        - at start date + interval (pass)
        - after start date + interval (pass)
        - at end date (pass)
        - after end date (pass)

    :return: (int, boolean, boolean)
    """

    release_interval = get_interval(settings.RELEASE_INTERVAL)

    mark_interval = get_interval(settings.MARK_INTERVAL)

    # start datetime
    start = get_datetime(settings.START_DATETIME)

    # end datetime
    end = get_datetime(settings.END_DATETIME)

    # current datetime
    current = get_current_datetime()

    # marking interval flag (assumes default as false)
    mark = False

    # mystery ended flag
    mystery_end = current >= end

    # release number counter
    release = 0

    # datetime counter
    date_time = start

    # calculates the current release
    while date_time <= current and date_time < end:
        mark = False
        release += 1
        date_time += release_interval

        # checks if date_time is still valid
        if date_time <= current and date_time < end:
            # toggles mark flag
            mark = True
            date_time += mark_interval

    return release, mark, mystery_end
