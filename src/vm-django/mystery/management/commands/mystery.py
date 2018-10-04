import os
import re
from shutil import copyfile
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from mystery.models import Mystery, Release


STATIC_DIR = os.path.join("mystery", "static", "mystery")


def get_release_number(rname):
    """
    Extracts release number from release name.

    Format: Release#

    :param rname: release name (string)
    :return: release number (int)
    """

    return re.findall('^.*?(\d+)$', rname)[0]


def create_mystery(name):
    """
    Creates mystery objects based on mystery folder info.

    :param name: mystery name (string)
    :return: returns mystery object hash attribute
    """
    mystery, _ = Mystery.objects.get_or_create(
        name=name,
    )

    return mystery.hash


def create_mystery_folder(mhash):
    """
    Creates mystery folder in django static folder.

    :param mhash: mystery objects hash attribute
    """
    abs_path = os.path.join(settings.BASE_DIR, STATIC_DIR, mhash)
    if not os.path.exists(abs_path):
        os.mkdir(abs_path)


def create_release(number, ans, clue, mname):
    """
    Creates release object based on release folder info.

    :param number: release number (int)
    :param ans: answer text (string)
    :param clue: clue test (string)
    :param mname: mystery name (string)
    :return: (mystery hash (string), release hash (string))
    """

    mystery = Mystery.objects.get(
        name=mname,
    )

    release, _ = Release.objects.get_or_create(
        mystery=mystery,
        number=number,
        clue=clue,
        answer=ans,
    )

    return mystery.hash, release.hash


def create_release_folder(mhash, rhash):
    """
    Creates release folder in django static folder.
    """
    abs_path = os.path.join(settings.BASE_DIR, STATIC_DIR, mhash, rhash)
    if not os.path.exists(abs_path):
        os.mkdir(abs_path)


def move_images(mhash, rhash, rpath, nimages):
    """
    Moves images from release folder to release hash folder in static folder.
    :param mhash: mystery hash (string)
    :param rhash: release hash (string)
    :param rpath: release folder absolute path (string)
    :param nimages: number of images in release folder (int)
    """
    abs_path = os.path.join(settings.BASE_DIR, STATIC_DIR, mhash, rhash)
    if os.path.exists(abs_path):
        while nimages != 0:
            image = "image" + str(nimages) + ".jpg"
            copyfile(os.path.join(rpath, image),
                     os.path.join(abs_path, image))
            nimages -= 1


class Command(BaseCommand):
    """
    Assign command - used to create mystery app instance models and connections
    from file.

    File Type: csv

    Format: PRA,Group,Mystery
    """
    help = "Used to create mystery app mystery and release objects and " \
           "connections from formatted folder. Parses folder and extracts " \
           "required information. Copies static files to static folder. " \
           "Using mystery hash format."

    def add_arguments(self, parser):
        """
        adding command arguments to command line parser.
        """
        parser.add_argument('folder_path', type=str)

    def handle(self, *args, **options):
        """
        Parses mystery folder structure and creates mystery app mystery
        and release models as well as hashed mystery static file folder
        structure.
        """
        # root mysteries folder path
        fpath = options['folder_path']

        try:
            if os.path.isdir(fpath):
                # traverses files top to bottom recursively from fpath
                for root, dirs, files in os.walk(fpath):
                    try:
                        # ans.txt text
                        ans = ""
                        # clue.txt test
                        clue = ""
                        # image counter
                        nimages = 0

                        # release folder
                        if files:
                            # print(os.path.basename(root))
                            # for files in release folder
                            for file_path in files:
                                # text file
                                if file_path.lower().endswith("clue.txt"):
                                    # clue file
                                    with open(os.path.join(root, file_path),
                                              'r') as file:

                                        # saves clue
                                        clue = file.read()

                                elif file_path.lower().endswith("ans.txt"):
                                    # answer file
                                    with open(os.path.join(root, file_path),
                                              'r') as file:

                                        # saves answer
                                        ans = file.read()

                                elif file_path.lower().endswith("jpg"):
                                    # image file

                                    # increments image counter
                                    nimages += 1

                            # create release object

                            # release number
                            rnumber = get_release_number(
                                os.path.basename(root)
                            )
                            # mystery name
                            mname = os.path.basename(os.path.dirname(root))
                            # create release
                            mhash, rhash = create_release(rnumber, ans, clue,
                                                          mname)
                            # creates release static folder
                            create_release_folder(mhash, rhash)
                            # moves images to release static folder
                            move_images(mhash, rhash, root, nimages)

                        # mystery folder
                        elif root != fpath:
                            # creates mystery object
                            mhash = create_mystery(os.path.basename(root))
                            # creates mystery static folder
                            create_mystery_folder(mhash)

                    except IndexError:
                        # problem extracting release number
                        self.stderr.write(self.style.WARNING(
                            "Release Number Error: {}".format(
                                os.path.basename(root))))
                    except IntegrityError:
                        # duplicate information
                        if files:
                            # release being processed
                            self.stderr.write(self.style.WARNING(
                                "Duplicate Information: {} {}".format(
                                    # mystery name
                                    os.path.basename(os.path.dirname(root)),
                                    # release name
                                    os.path.basename(root)
                                )))
                        else:
                            # mystery being processed
                            self.stderr.write(self.style.WARNING(
                                "Duplicate Information: {}".format(
                                    # mystery name
                                    os.path.basename(root)
                                )))
                    except ObjectDoesNotExist:
                        # queried object does not exist
                        if files:
                            # release being processed
                            self.stderr.write(self.style.WARNING(
                                "ObjectDoesNotExist: {} {}".format(
                                    # mystery name
                                    os.path.basename(os.path.dirname(root)),
                                    # release name
                                    os.path.basename(root)
                                )))
                        else:
                            # mystery being processed
                            self.stderr.write(self.style.WARNING(
                                "ObjectDoesNotExist: {}".format(
                                    # mystery name
                                    os.path.basename(root)
                                )))
                    except OSError:
                        if files:
                            # release being processed
                            self.stderr.write(self.style.WARNING(
                                "An Error Occurred: {} {}".format(
                                    # mystery name
                                    os.path.basename(os.path.dirname(root)),
                                    # release name
                                    os.path.basename(root)
                                )))
                        else:
                            # mystery being processed
                            self.stderr.write(self.style.WARNING(
                                "An Error Occurred: {}".format(
                                    # mystery name
                                    os.path.basename(root)
                                )))
            else:
                # fpath not a path to folder
                self.stderr.write(self.style.ERROR("Provided path is not a "
                                                   "folder."))
        except FileNotFoundError:
            # file path does not exist
            self.stderr.write(self.style.ERROR("File does not exist."))
        except OSError:
            # error occurred during folder structure traversal
            self.stderr.write(self.style.ERROR(
                "Error during folder traversal."))



