import os

from datetime import datetime


MEDIA_DATA = {}


def partition_media(root_dir):
    """Group media files and sort them by date and time."""
    # Grab media files meta data.
    get_file_data(root_dir)

    # Construct filename based on date and time.
    # Store original and constructed filename in csv format.
    # Write csv file.
    # Return reconstructed filenames.


def get_file_data(dir):
    """Return media files meta data."""
    cme = [  # Common Media File Extensions
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".sv",
        ".mp4", ".avi", ".mkv", ".flv", ".webm", ".h264", ".h265",
        ".flac", ".wav", ".aiff", ".mp3", ".aac", ".ogg"
    ]

    # Pull media filepaths.
    tree_path = os.walk(dir)
    for dir, _, files in tree_path:
        for file in files:
            for ext in cme:
                if file.endswith(ext):
                    MEDIA_DATA[file] = {
                        'original_name': file,
                        'path': dir,
                        'full_path': os.path.join(dir, file)
                    }; break

    # Read date & time from files meta data.
    for file in MEDIA_DATA:
        fp = MEDIA_DATA[file]['full_path']
        # Most recent content modification.
        raws = os.stat(fp).st_mtime
        rtime = datetime.fromtimestamp(raws)
        MEDIA_DATA[file]['date_created'] = {
            'Month': rtime.strftime("%m"),
            'Day': rtime.strftime("%d"),
            'Year': rtime.strftime("%y"),
            'Week': rtime.strftime("%a"),
            'Hour': rtime.strftime("%H"),
            'Minute': rtime.strftime("%M"),
            'Second': rtime.strftime("%S"),
            'Raw(Seconds)': raws,
            'Full': rtime.strftime("%m/%d/%y %a %H:%M:%S")
        }

    ri = list(MEDIA_DATA.keys())[-1]
    print(MEDIA_DATA[ri])
