import csv
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.core.management.base import BaseCommand, CommandError
from system.models import Practical, Group

# user model
UserModel = get_user_model()


def create_pra(name):
    """
    Creates and saves practical object.
    """
    practical, created = Practical.objects.get_or_create(
        name=name,
    )

    return practical


def create_group(name, practical):
    """
    Creates and saves group objects.
    """
    group, created = Group.objects.get_or_create(
        name=name,
        practical=practical
    )

    return group


def create_user(uname, group):
    """
    Creates and saves user objects.
    """
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
    System command - used to create system app models and connections from csv
    file.
    """
    help = 'system command info.'

    def add_arguments(self, parser):
        """
        adding command arguments to command line parser.
        """
        parser.add_argument('csv_path', type=str)

    def handle(self, *args, **options):
        """
        *description*
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
                            practical = create_pra(row[1])
                            group = create_group(row[2], practical)
                            _ = create_user(row[0], group)
                        except IntegrityError:
                            self.stderr.write(
                                "Duplicate Information: {}".format(row))
                        except IndexError:
                            # problem extracting missing information
                            self.stderr.write("Format Error: {}".format(row))
                        except ValueError:
                            self.stderr.write("ValueError: {}".format(row))
            else:
                # file not csv
                self.stderr.write("File not of type csv.")

        except FileNotFoundError:
            # problem opening file
            self.stderr.write("File does not exist.")



