import re
from models import Song


def tracklist_parser(filename):
    """Load new tracklist from file to DB.

    :param filename: tracklist filename
    """
    sep, tracklist = ' - ', []
    with open(filename, encoding='utf-8-sig') as f:
        for line in f:
            line = re.sub(r'\d+\. ', '', line)
            author_song = line.rstrip().split(sep=sep)
            # read pair "author - song title"
            tracklist.append(tuple(author_song))
    Song.objects.bulk_create([Song(author=track[0], song=track[1])
                              for track in tracklist])


tracklist_parser('tracklist.txt')