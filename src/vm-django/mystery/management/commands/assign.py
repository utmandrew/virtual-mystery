import csv
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from mystery.models import Instance, Mystery
# dependant on system group model
from system.models import Group


def create_instance(practical, group, mystery):
    """
    Creates and saves the object if it does not exist, otherwise it gets the
    existing object.

    :param practical: practical name
    :param mystery: mystery name
    :param group: group name
    """
    _group = Group.objects.get(
        practical__name=practical,
        name=group
    )

    _mystery = Mystery.objects.get(
        name=mystery
    )

    Instance.objects.get_or_create(
        group=_group,
        mystery=_mystery
    )


class Command(BaseCommand):
    """
    Assign command - used to create mystery app instance objects and
    connections from file.

    File Type: csv

    Format: PRA,Group,Mystery
    """

    help = 'Used to create mystery app instance objects and connections from '\
           'csv file (Format: PRA,Group,Mystery)'

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
                        try:
                            create_instance(row[0].strip(), row[1].strip(),
                                            row[2].strip())
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
                        except ObjectDoesNotExist:
                            # queried object does not exist
                            self.stderr.write(self.style.WARNING(
                                "(Warning) "
                                "ObjectDoesNotExist: {}".format(row)))
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
