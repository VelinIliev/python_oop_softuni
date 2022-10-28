class Music:
    def __init__(self, title: str, artist: str, lyrics: str):
        title = title
        artist = artist
        lyrics = lyrics

    def print_info(self):
        return f'This is "{title}" from "{artist}"'

    def play(self):
        return lyrics


song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())
