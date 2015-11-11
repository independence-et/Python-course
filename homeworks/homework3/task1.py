from task0 import Song
from task0 import import_songs
__author__ = 'Independence'


# creating lists:
songs = import_songs("songs1.txt")
artists = list()
artist_count = list()
albums = list()
album_count = list()
album_duration = list()
duration = list()
words = list()
word_count = list()
artist_album_count = list()

# main cycle(counting it all):
for song in songs:
    # counting artists:
    if song.artist not in artists:
        artists.append(song.artist)
        artist_count.append(1)
        artist_album_count.append(0)
    else:
        artist_count[artists.index(song.artist)] += 1
    # counting albums:
    if (song.album, song.artist) not in albums:
        albums.append((song.album, song.artist))
        album_count.append(1)
        album_duration.append(int(song.duration))
        artist_album_count[artists.index(song.artist)] += 1
    else:
        album_count[albums.index((song.album, song.artist))] += 1
        album_duration[albums.index((song.album, song.artist))] += \
            int(song.duration)
    # counting and checking words:
    a = song.name.split(" ")
    for word in a:
        if len(word) > 0:
            word2 = word.lower()
            x = True
            for i in range(len(word)):
                if word2[i] not in "abcdefghijklmnopqrstuvwxyz":
                    x = False
            if x is False:
                continue
            if word2 not in words:
                words.append(word2)
                word_count.append(1)
            else:
                word_count[words.index(word2)] += 1
    duration.append(int(song.duration))

# resulting:
long_song = (songs[duration.index(max(duration))])
long_album = albums[album_duration.index(max(album_duration))]
freq_words = str()
i = 0
while i < 10 and i < len(words)-1:
    freq_words = freq_words + words[word_count.index(max(word_count))] + "\t"
    words.remove(words[word_count.index(max(word_count))])
    word_count.remove(word_count[word_count.index(max(word_count))])
    i += 1

# output:
print(artists[artist_count.index(max(artist_count))])
print(long_song.name, "\t", long_song.artist)
print(long_album[0], "\t", long_album[1])
print(freq_words)
print(artists[artist_album_count.index(max(artist_album_count))])
