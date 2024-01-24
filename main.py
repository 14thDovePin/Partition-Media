"""TODO LIST
- Implement configuration file.
    - Implement `config.ini` check system.
- Implement file and folder management.
- Implement sorting algorithm.
- Implement naming system.
    - Rename files based on their date and time meta data.
    - Store the original file names using the csv data structure.
"""


import os

from configparser import ConfigParser


CONFIG = ConfigParser()
CONFIG_FN = "config.ini"
CONFIG_DIR = os.path.join(os.getcwd(), CONFIG_FN)


def main():
    """The main function of the script."""
    # Configure script.
    configuration()


def configuration():
    """Manage the script's configuration."""
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
    config = CONFIG['CONFIGURATION']


if __name__ == '__main__':
    main()
