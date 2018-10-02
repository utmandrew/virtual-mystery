import os
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """
    Assign command - used to create mystery app instance models and connections
    from file.

    File Type: csv

    Format: PRA,Group,Mystery
    """
    help = ""

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
                    # release folder
                    if files:
                        print(os.path.basename(root))
                        # for files in release folder
                        for file_path in files:
                            # text file
                            if file_path.endswith("txt"):
                                file = open(os.path.join(root, file_path), 'r')

                                print(file_path)

                                # for line in file:
                                #     print(line)

                                print(file.read())

                                file.close()
                    # mystery folder
                    elif root != path:
                        print("Mystery " + os.path.basename(root))
            else:
                # fpath not a path to folder
                pass
        except:
            pass



