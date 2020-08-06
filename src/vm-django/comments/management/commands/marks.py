import os
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from comments.models import Result
from mystery.models import Release

# private directory relative path
STATIC_DIR = os.path.join("system", "private")
# makes static dir if it doesn't already exist
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)

# user model
UserModel = get_user_model()


def log_marks(row):
    """
    Writes formatted string to a csv file.

    :param row: string
    :return: None
    """
    fpath = os.path.join(settings.BASE_DIR, STATIC_DIR, "marks.csv")

    if os.path.exists(fpath):
        # file exists
        mode = 'a'
    else:
        # file d.n.e
        mode = 'w+'

    with open(fpath, mode) as file:
        file.write(row + "\n")


def create_row(username, results, release_count):
    """
    Returns string with format UserName,M1,M2,...,Mn.
    :param username: string
    :param results: queryset object
    :param release_count: int
    :return: Formatted string
    """
    row = "{}".format(username)

    count = 1
    while count <= release_count:
        result = results.filter(comment__release=count).first()

        if result:
            row += ",{}".format(result.mark)
        else:
            row += ",0"
        count += 1

    return row


def count_releases(mystery):
    """
    Returns the number of release objects associated with the mystery.
    :param mystery: mystery object
    :return: int
    """
    return Release.objects.filter(mystery=mystery).count()


class Command(BaseCommand):
    """
    Marks command - used to extract user marks for each release.

    Format: UserName, M1, M2, ..., Mn

    Note:
        - Assumes release numbers start at 1 and increment by 1
    """

    help = 'Used to extract user marks. No arguments required.'

    def handle(self, *args, **options):
        """
        Queries all student users and iteratively passes them onto the
        log_marks helper function.
        """
        try:
            users = UserModel.objects.filter(is_staff=False, is_ta=False)
            for user in users:
                try:
                    # number of releases in users mystery
                    release_count = count_releases(
                        user.group.instance.all().first().mystery)

                    # users results objects
                    results = Result.objects.filter(comment__owner=user). \
                        order_by('comment__release')

                    # creates formatted row for csv
                    row = create_row(user.username, results, release_count)

                    # writes row to csv file
                    log_marks(row)

                except AttributeError:
                    # error while getting user mystery
                    self.stderr.write(
                        self.style.WARNING("(Warning) error during mark "
                                           "extraction: {}".format(user.username)))
                except IOError:
                    # error writing file
                    self.stderr.write(
                        self.style.ERROR("(Warning) Problem writing"
                                         " to file: {}".format(user.username)))

            # prints users.txt file path
            self.stdout.write("Marks File Location: {}".format(
                os.path.join(settings.BASE_DIR, STATIC_DIR, "marks.csv")
            ))

        except IOError:
            # error writing file
            self.stderr.write(
                self.style.ERROR("(Error) IOError."))
