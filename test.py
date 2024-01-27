''' Test suite checklist.
Setup 25 sample files for testing.
    - ? Generate files with custom meta data.
    - Check meta data.
    - Check constructed filenames.
'''


import os
import unittest

from main import configuration


class TestStringMethods(unittest.TestCase):

    def test_config_ini(self):
        # Assuem expected contents.
        expected = [
        '[CONFIGURATION]',
        'manual_input_mode',
        'default_sorting_directory',
        'max_file_count_per_group',
        'segregate_file_types',
        'use_date_for_grouping',
        ]

        # Check and open `config.ini`.
        cfg_path = os.path.join(os.getcwd(), 'config.ini')
        if not os.path.exists(cfg_path):
            configuration()

        # TEST Check file presence.
        err_msg = 'File `config.ini` not found!'
        self.assertTrue(os.path.exists(cfg_path), err_msg)

        with open(cfg_path, 'r') as f:
            contents = f.readlines()

        # TEST Cross reference contents.
        for i, data in enumerate(expected):
            err_msg = f'Configuration key `{data}` mismatch!'
            self.assertTrue(data in contents[i], err_msg)


if __name__ == '__main__':
    unittest.main()
