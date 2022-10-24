from project.album import Album
from project.song import Song

class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        in_albums = False
        for x in self.albums:
            if x.name == album.name:
                in_albums = True
                return f'Band {self.name} already has {album.name} in their library.'
        if not in_albums:
            self.albums.append(album)
            return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name: str):
        for i, album in enumerate(self.albums):
            if album.name == album_name:
                if album.published:
                    return f'Album has been published. It cannot be removed.'
                else:
                    self.albums.pop(i)
                    return f'Album {album_name} has been removed.'
        return f'Album {album_name} is not found.'

    def details(self):
        return_string = ""
        return_string += f"Band {self.name}\n"
        for album in self.albums:
            return_string += f'{album.details()}\n'
        return return_string


# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())
