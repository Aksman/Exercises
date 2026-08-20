# EXERCISE
# Create a Song class and a Playlist container class for the songs.
# The Playlist class must have methods to add a Song, remove a Song,
# and shuffle its songs.

from datetime import timedelta
from random import shuffle

class Song:
    def __init__(self, title: str, artist: str, duration: str):
        self.title = title
        self.artist = artist
        minutes, seconds = duration.split(':')
        self.duration = timedelta(minutes=int(minutes), seconds=int(seconds))

    def __str__(self):
        return f"\"{self.title}\" by {self.artist}"

    def __repr__(self):
        return f"Song(\"{self.title}\", \"{self.artist}\", \"{self.durationStr()}\")"

    def durationStr(self):
        totalSeconds = int(self.duration.total_seconds())
        minutes, seconds = divmod(totalSeconds, 60)
        return f"{minutes}:{seconds:02d}"

class Playlist:
    def __init__(self):
        self.__order = []

    def add(self, *songs: Song):
        self.__order.extend(songs)

    def remove(self, songTitle: str) -> bool:
        for i, song in enumerate(self.__order):
            if song.title == songTitle:
                self.__order.pop(i)
                return True
        return False

    def __getitem__(self, songTitle: str) -> Song:
        for song in self.__order:
            if song.title == songTitle:
                return song
        return None

    def __iter__(self):
        return iter(self.__order)

    def shuffle(self):
        shuffle(self.__order)

    def __len__(self):
        runtime = timedelta(seconds=0)
        for song in self.__order:
            runtime += song.duration
        return int(runtime.total_seconds())

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    mixtape = Playlist()
    mixtape.add(Song("I'm So Sick", "Flyleaf", "2:55"),
           Song("Dear Agony", "Breaking Benjamin ft. Lacey Sturm", "4:19"),
           Song("And the Rest is Mystery", "Project Aegis", "9:07"),
           Song("crushcrushcrush", "Paramore", "3:10"),
           Song("Over You", "Daughtry", "3:45"))

    print("SONG LIST")
    print("=" * 9)
    for i, song in enumerate(mixtape, start=1):
        print(f"{i}. {song} ({song.durationStr()})")

    print()
    mixtape.remove('crushcrushcrush')
    mixtape.shuffle()
    print("SHUFFLED SONG LIST")
    print("=" * 18)
    for i, song in enumerate(mixtape, start=1):
        print(f"{i}. {song} ({song.durationStr()})")

    print()
    totalRuntime = len(mixtape)
    runtimeMinutes, runtimeSeconds = divmod(totalRuntime, 60)
    print(f"Total runtime: {runtimeMinutes}:{runtimeSeconds:02d}")
    