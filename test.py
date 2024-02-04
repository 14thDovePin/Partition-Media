''' TODO List
-
'''


import os
import unittest

from main import configuration
from partition_media import get_file_data


SAMPLES = os.path.join(os.getcwd(), 'Sample')

CMFE = [  # Common Media File Extensions
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".sv",
    ".mp4", ".avi", ".mkv", ".flv", ".webm", ".h264", ".h265",
    ".flac", ".wav", ".aiff", ".mp3", ".aac", ".ogg"
]

CFG_VAL = [  # Configuration Values
'[CONFIGURATION]',
'manual_input_mode',
'default_sorting_directory',
'max_file_count_per_group',
'segregate_file_types',
'use_date_for_grouping',
]

FD = {  # Old File Data
    'original_name': str(),
    'path': str(),
    'full_path': str(),
    'date_created' : {
        'Month': str(),
        'Day': str(),
        'Year': str(),
        'Week': str(),
        'Hour': str(),
        'Minute': str(),
        'Second': str(),
        'Raw(Seconds)': float(),
        'Full': str()
    }
}

# FD = {  # File Data
#     'i_name': str,  # Initial
#     'i_path': str,
#     'i_fp': str,    # Full Path
#     'n_name': str,  # New
#     'n_path': str,
#     'n_fp': str,
#     'date_created' : {
#         'month': str,
#         'day': str,
#         'year': str,
#         'week': str,  # Mon, Tue, ...
#         'hour': str,
#         'minute': str,
#         'second': str,
#         'raw': float,
#         'full': str  # MM/DD/YY W HH:MM:SS
#     }
# }


class TestStringMethods(unittest.TestCase):

    def test_config_ini(self):
        """Test configuration file."""
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
        for i, data in enumerate(CFG_VAL):
            err_msg = f'Configuration key `{data}` mismatch!'
            self.assertTrue(data in contents[i], err_msg)

    def test_samples(self):
        """Test sample directory and its contents."""
        # TEST Check samples directory.
        err_msg = 'Directory `Samples` not found!'
        self.assertTrue(os.path.exists(SAMPLES), err_msg)

        filepaths = []
        contents = os.walk(SAMPLES)
        for path, _, files in contents:
            for file in files:
                f = os.path.join(path, file)
                filepaths.append(f)

        # TEST Check media contents.
        media_file_count = 0
        for file in filepaths:
            for ext in CMFE:
                if file.endswith(ext):
                    media_file_count += 1
        err_msg = 'No sample media files found!\n.'
        self.assertTrue(media_file_count > 0, err_msg)

    def test_filepath_filedata(self):
        """Test filepath handling and filedata structure."""
        # Give samples to test.
        samples_data = get_file_data(SAMPLES)
        file_data = [samples_data[i] for i in samples_data]

        # Expected keys and value types.
        exp_fdk = list(FD.keys())
        exp_fdk2 = FD[exp_fdk[-1]].keys()
        exp_fdv = [type(i) for i in FD.values()]
        exp_fdv2 = [type(i) for i in FD[exp_fdk[-1]].values()]

        err_msg1 = 'File data dictionary error, key mismatch.'
        err_msg2 = 'File data dictionary error, type mismatch.'
        err_msg3 = 'File does not exist!'

        for fd in file_data:
            # Grab generated keys and value types.
            gen_fdk = list(fd.keys())
            gen_fdk2 = fd[gen_fdk[-1]].keys()
            gen_fdv = [type(i) for i in fd.values()]
            gen_fdv2 = [
                type(i) for i in fd[gen_fdk[-1]].values()
                ]

            # TEST Check keys of the data structure.
            self.assertEqual(exp_fdk, gen_fdk, err_msg1)
            self.assertEqual(exp_fdk2, gen_fdk2, err_msg1)

            # TEST Check values type of data structure.
            self.assertEqual(exp_fdv, gen_fdv, err_msg2)
            self.assertEqual(exp_fdv2, gen_fdv2, err_msg2)

            # TEST Check if file exists.
            # TODO: Update 'path' to 'i_fp'.
            self.assertTrue(os.path.exists(fd['path']), err_msg3)


if __name__ == '__main__':
    unittest.main()
