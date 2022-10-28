from project.song import Song

class Album:
    def __init__(self, name: str, *songs):
        name = name
        songs = [*songs]
        published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif published:
            return f'Cannot add songs. Album is published.'
        else:
            already_in_album = False
            for x in songs:
                if x.name == song.name:
                    already_in_album = True
            if already_in_album:
                return f'Song is already in the album.'
            else:
                songs.append(song)
                return f'Song {song.name} has been added to the album {name}.'

    def remove_song(self, song_name: str):
        in_album = False
        if published:
            return f'Cannot remove songs. Album is published.'
        for i, x in enumerate(songs):
            if x.name == song_name:
                in_album = True
                songs.pop(i)
                return f'Removed song {song_name} from album {name}.'
        if not in_album:
            return f'Song is not in the album.'

    def publish(self):
        if published:
            return f'Album {name} is already published.'
        else:
            published = True
            return f'Album {name} has been published.'

    def details(self):
        return_string = ""
        return_string += f"Album {name}\n"
        for x in songs:
            return_string += f'== {x.get_info()}\n'
        return return_string