"""TODO LIST
- Implement configuration file.
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
    if not os.path.exists(CONFIG_DIR):
        create_config()
        print("Configuration File Created!")


def create_config():
    """Create the configuration file."""
    # Construct configuration.
    CONFIG['CONFIGURATION'] = {
        'manual_input_mode': 'true',
        'default_sorting_directory': 'None',
        'max_file_count_per_group': '20',
        'segregate_file_types': 'false',
        'use_date_for_grouping': 'false',
        }

    # Write configuration.
    with open(CONFIG_DIR, 'w') as f:
        CONFIG.write(f)


if __name__ == '__main__':
    main()
