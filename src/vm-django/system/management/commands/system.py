import csv
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.core.management.base import BaseCommand, CommandError
from system.models import Practical, Group

# user model
UserModel = get_user_model()


def create_pra(name):
    """
    Returns practical object. Creating and saving the object if it does not
    exist, otherwise it gets the existing object.

    :param name: practical name
    :return: practical object
    """
    practical, created = Practical.objects.get_or_create(
        name=name,
    )

    return practical


def create_group(name, practical):
    """
    Returns group object. Creating and saving the object if it does not exist,
    otherwise it gets the existing object.

    :param name: group name
    :param practical: practical object
    :return: group object
    """
    group, created = Group.objects.get_or_create(
        name=name,
        practical=practical
    )

    return group


def create_user(uname, group):
    """
    Returns the newly created and saved user object.

    :param group: group object
    :param uname: user name
    :return: user object
    """
    # temporary password (for testing)
    passwd = 'HelloMoto123'

    # creates user
    user = UserModel.objects.create_user(
        username=uname,
        password=passwd,
        group=group
    )

    # saves user
    user.save()

    return user


class Command(BaseCommand):
    """
    System command - used to create system app objects and connections from
    file.

    File Type: csv

    Format: User,PRA,Group
    """

    help = 'Used to create system app objects and connections from csv file ' \
           '(Format: User,PRA,Group)'

    def add_arguments(self, parser):
        """
        adding command arguments to command line parser.
        """
        parser.add_argument('csv_path', type=str)

    def handle(self, *args, **options):
        """
        Parses csv file and creates corresponding objects from parsed data.
        Note: parsed data in csv format
        """
        try:
            # csv path argument
            fpath = options['csv_path']
            # checks if file is csv
            if fpath.lower().endswith('csv'):
                with open(fpath) as file:
                    reader = csv.reader(file, delimiter=",")
                    # iterating through each row in csv
                    for row in reader:
                        # creates system model objects
                        try:
                            # csv entries are stripped of leading and trailing
                            # whitespace
                            practical = create_pra(row[1].strip())
                            group = create_group(row[2].strip(), practical)
                            _ = create_user(row[0].strip(), group)
                        except IntegrityError:
                            # duplicate information
                            self.stderr.write(self.style.WARNING(
                                "Duplicate Information: {}".format(row)))
                        except IndexError:
                            # problem extracting missing information
                            self.stderr.write(self.style.WARNING(
                                "Format Error: {}".format(row)))
                        except ValueError:
                            # missing information
                            self.stderr.write(self.style.WARNING(
                                "ValueError: {}".format(row)))
            else:
                # file not csv
                self.stderr.write(self.style.ERROR("File not of type csv."))

        except FileNotFoundError:
            # file path does not exist
            self.stderr.write(self.style.ERROR("File does not exist."))



