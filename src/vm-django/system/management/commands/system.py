import os
import csv
import chardet
from random import SystemRandom
from string import ascii_uppercase, digits
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.core.management.base import BaseCommand, CommandError
from system.models import Practical, Group

# private directory relative path
STATIC_DIR = os.path.join("system", "private")
# makes static dir if it doesn't already exist
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)

# user model
UserModel = get_user_model()


def get_encoding(fname):
    """
    Returns encoding of file, fname.
    :param fname: string
    :return: string
    """
    file = open(fname, 'rb')
    encoding = chardet.detect(file.read())['encoding']
    return encoding


def user_credentials(uname, password, email):
    """
    Creates/opens a csv file and appends the newly created user's username,
    password and email into the file.
    :param uname: username (string)
    :param password: password (string)
    :param email: email (string)
    """
    fpath = os.path.join(settings.BASE_DIR, STATIC_DIR, "users.csv")

    if os.path.exists(fpath):
        # file exists
        mode = 'a'
    else:
        # file d.n.e
        mode = 'w+'

    with open(fpath, mode) as file:
        file.write("{},{},{}\n".format(uname, password, email))


def generate_password():
    """
    Returns a random 8 digit string consisting of numbers [0-9] and uppercase
    letters [A-Z].
    :return: random 8 char (string)
    """
    return ''.join(SystemRandom().choice(ascii_uppercase + digits)
                   for _ in range(8))


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


def create_user(uname, fname, email, group):
    """
    Returns the newly created and saved user object.

    :param group: group object
    :param uname: username
    :param fname: user first name
    :param email: user email
    :return: password string
    """
    password = generate_password()

    # creates user
    user = UserModel.objects.create_user(
        username=uname,
        first_name=fname,
        email=email,
        password=password,
        group=group
    )

    # saves user
    user.save()

    # saves user credentials
    user_credentials(uname, password, email)

    return user


class Command(BaseCommand):
    """
    System command - used to create system app objects and connections from
    file.

    File Type: csv

    Format: User,FirstName,PRA,Group,Email
    """

    help = 'Used to create system app objects and connections from csv file ' \
           '(Format: User,FirstName,PRA,Group,Email)'

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
                encoding = get_encoding(fpath)
                with open(fpath, encoding=encoding) as file:
                    reader = csv.reader(file, delimiter=",")
                    # iterating through each row in csv
                    for row in reader:
                        # creates system model objects
                        try:
                            # csv entries are stripped of leading and trailing
                            # whitespace
                            practical = create_pra(row[2].strip())
                            group = create_group(row[3].strip(), practical)
                            _ = create_user(row[0].strip(), row[1].strip(),
                                            row[4].strip(), group)

                        except IntegrityError:
                            # duplicate information
                            self.stderr.write(self.style.WARNING(
                                "(Warning) "
                                "Duplicate Information: {}".format(row)))
                        except IndexError:
                            # problem extracting missing information
                            self.stderr.write(self.style.WARNING(
                                "(Warning) Incorrect Format: {}".format(row)))
                        except ValueError:
                            # missing information
                            self.stderr.write(self.style.WARNING(
                                "(Warning) Missing Value: {}".format(row)))

                # prints users.txt file path
                self.stdout.write("User File Location: {}".format(
                    os.path.join(settings.BASE_DIR, STATIC_DIR, "users.csv")
                ))

            else:
                # file not csv
                self.stderr.write(self.style.ERROR("(Error) "
                                                   "File not of type csv."))

        except FileNotFoundError:
            # file path does not exist
            self.stderr.write(self.style.ERROR("(Error) File does not exist."))
        except IOError:
            # error reading file
            self.stderr.write(self.style.ERROR("(Error) Error reading file."))


