"""TODO LIST
- Implement configuration file.
    - Implement `config.ini` check system.
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
from sys import exit


CONFIG = ConfigParser()
CONFIG_FN = "config.ini"
CONFIG_DIR = os.path.join(os.getcwd(), CONFIG_FN)


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
    reconstruct_filenames(root_dir)


def reconstruct_filenames(root_dir):
    """Return reconstructed filenames."""
    cme = [  # Common Media Extensions
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".sv",
        ".mp4", ".avi", ".mkv", ".flv", ".webm", ".h264", ".h265",
        ".flac", ".wav", ".aiff", ".mp3", ".aac", ".ogg"
    ]

    # Pull media filepaths.
    media_file_paths = []
    original_filenames = []
    tree_path = os.walk(root_dir)
    for dir, _, files in tree_path:
        for file in files:
            for ext in cme:
                if file.endswith(ext):
                    filepath = os.path.join(dir, file)
                    media_file_paths.append(filepath)
                    original_filenames.append(file)
                    break

    # Read files metadata.
    # Construct filename based on date and time.
    # Store original and constructed filename in csv format.
    # Write csv file.
    # Return reconstructed filenames.


def configuration():
    """Construct and/or return script's configuration."""
    if not os.path.exists(CONFIG_DIR):

        # Construct and write the config file.
        CONFIG['CONFIGURATION'] = {
            'manual_input_mode': 'True',
            'default_sorting_directory': 'None',
            'max_file_count_per_group': '20',
            'segregate_file_types': 'False',
            'use_date_for_grouping': 'False',
            }
        with open(CONFIG_DIR, 'w') as f:
            CONFIG.write(f)
        print("Configuration File Created!")

    # Read config file.
    CONFIG.read(CONFIG_DIR)
    return CONFIG['CONFIGURATION']


if __name__ == '__main__':
    main()
