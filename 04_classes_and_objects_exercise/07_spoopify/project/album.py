from project.song import Song

class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = [*songs]
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f'Cannot add songs. Album is published.'

        if song in self.songs:
            return f'Song is already in the album.'
        else:
            self.songs.append(song)
            return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        if self.published:
            return f'Cannot remove songs. Album is published.'
        song = next(filter(lambda x: x.name == song_name, self.songs), None)
        if song:
            self.songs.remove(song)
            return f'Removed song {song_name} from album {self.name}.'

        return f'Song is not in the album.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'
        else:
            self.published = True
            return f'Album {self.name} has been published.'

    def details(self):
        output = [f"Album {self.name}"]
        for song in self.songs:
            output.append(f'== {song.get_info()}')
        return '\n'.join(output)
