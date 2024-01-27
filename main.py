"""TODO LIST
- Implement configuration file.
    - Implement `config.ini` check system.
    - Add option for most recent content modification
    option instead of creation.
- Implement file and folder management.
- Implement sorting algorithm.
- Implement naming system.
    - Rename files based on their date and time meta data.
    - Store the original file names using the csv data structure.
- Store the original and the reconstructed filenames in csv format.
    - Use only 1 csv data bank.
    - Back up csv data bank.
- Implement cap system i.e. for accidental sort on whole disk.
"""


import os

from configparser import ConfigParser
from datetime import datetime
from sys import exit

from partition_media import partition_media


CONFIG = ConfigParser()
CONFIG_FN = "config.ini"
CONFIG_DIR = os.path.join(os.getcwd(), CONFIG_FN)
MEDIA_FILEPATHS = {}


def main():
    """The main function of the script."""
    # Configure script.
    config = configuration()

    # Grab root directory to modify.
    if config.getboolean('manual_input_mode'):
        print('Input root directory to partition.')
        while True:
            root_dir = input('RootDirectory-> ')
            if not os.path.exists(root_dir):
                print('InvalidDirectory!')
            else: break
    else:
        root_dir = config.get('default_sorting_directory')
        if not os.path.exists(root_dir):
            print('ConfigurationError! "default_sorting_directory" is'
                  ' not a valid directory. Press Enter to exit.')
            input(); exit()

    # Manage file names.
    partition_media(root_dir)


def configuration():
    """Construct and/or return script's configuration."""
    if not os.path.exists(CONFIG_DIR):

        # Construct and write the config file.
        CONFIG['CONFIGURATION'] = {
            'manual_input_mode': 'true',
            'default_sorting_directory': 'None',
            'max_file_count_per_group': '20',
            'segregate_file_types': 'false',
            'use_date_for_grouping': 'false',
            }
        with open(CONFIG_DIR, 'w') as f:
            CONFIG.write(f)
        print("Configuration File Created!")

    # Read config file.
    CONFIG.read(CONFIG_DIR)
    return CONFIG['CONFIGURATION']


if __name__ == '__main__':
    main()
