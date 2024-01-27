import os

from datetime import datetime


def partition_media(root_dir):
    """Group media files and sort them by date and time."""
    # Grab media files meta data.
    media_data = get_file_data(root_dir)

    # Construct filename based on date and time.
    constructed_filepaths = construct_filenames(media_data)

    # Store original and constructed filename in csv format.
    # Write csv file.
    # Return reconstructed filenames.


def construct_filenames(md):
    """Return the constructed file names."""
    constructed_filepaths = []
    week_table = [
        'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'
    ]

    # Loop through all full filepaths.
    for i in md.values():
        new_filename = ''

        # Construct new filename using date and time creation.
        dnt = i['date_created']
        concatinate = [
            dnt['Month'],
            dnt['Day'],
            dnt['Year'],
            str(week_table.index(dnt['Week'])+1),
            dnt['Hour'],
            dnt['Minute'],
            dnt['Second'],
            '.' + i['original_name'].split('.')[-1]
        ]
        new_filename = ''.join(concatinate)

        # For files that were created within he same second.
        # Overflow check.


        # Construct new full filepath & append.
        final = os.path.join(i['path'], new_filename)
        constructed_filepaths.append(final)

    print(constructed_filepaths[-1])
    return constructed_filepaths


def get_file_data(dir):
    """Grab media files meta data."""
    cme = [  # Common Media File Extensions
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".sv",
        ".mp4", ".avi", ".mkv", ".flv", ".webm", ".h264", ".h265",
        ".flac", ".wav", ".aiff", ".mp3", ".aac", ".ogg"
    ]
    media_data = {}

    # Pull media filepaths.
    tree_path = os.walk(dir)
    for dir, _, files in tree_path:
        for file in files:
            for ext in cme:
                if file.endswith(ext):
                    media_data[file] = {
                        'original_name': file,
                        'path': dir,
                        'full_path': os.path.join(dir, file)
                    }; break

    # Read date & time from files meta data.
    for file in media_data:
        fp = media_data[file]['full_path']
        # Most recent content modification.
        raws = os.stat(fp).st_mtime
        rtime = datetime.fromtimestamp(raws)
        media_data[file]['date_created'] = {
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

    return media_data
