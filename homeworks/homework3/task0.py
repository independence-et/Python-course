__author__ = 'Independence'


class Song:
    def __init__(self, name, artist, album, position, year, duration):
        self.name = name
        self.artist = artist
        self.album = album
        self.position = position
        self.year = year
        self.duration = duration

    def __repr__(self):
        if int(self.duration) > 0:
            return "Song \"%s\" by %s" % (self.name, self.artist) \
                   + '(' + self.duration + ' sec)'
        return "Song \"%s\" by %s" % (self.name, self.artist)
        # return(self.name + " " + self.artist)

    def __lt__(self, other):
        if self.artist < other.artist:
            return True
        if self.artist == other.artist and self.name < other.name:
            return True
        if self.artist == other.artist and self.name == other.name and\
           self.duration < other.duration:
            return True
        return False


def import_songs(filename):
    file0 = open(filename, "r")
    file1 = (file0.read()).replace("\n", "\t")
    file2 = file1.split('\t')
    i = 0
    file3 = list()
    while i < (len(file2)-1):
        file3.append(Song(file2[i], file2[i + 1], file2[i + 2],
                          file2[i + 3], file2[i + 4], file2[i + 5]))
        i += 6
    return file3


def export_songs(songs, filename):
    file = open(filename, "w")
    for song in songs:
        str0 = song.name + '\t' + song.artist + '\t' + song.album + '\t' + \
            song.position + '\t' + str(song.year) + '\t' +\
            str(song.duration) + '\t'
        file.write(str0)


def shuffle_songs(songs):
    from random import shuffle
    shuffle(songs)
    return songs


x = import_songs("songs1.txt")
shuffle_songs(x)
export_songs(x, 'songs2.txt')

# Unfortunately, this code doesn't works with full file on my computer:
# PyCharm some has problems with coding,
# so this code was tested only on a first part of this file
#  (part without "strange" symbols)
